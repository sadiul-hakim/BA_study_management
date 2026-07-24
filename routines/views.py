from datetime import timedelta

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.utils import timezone

from .models import Habit, HabitLog


def today_view(request):
    today = timezone.localdate()
    habits = Habit.objects.filter(is_active=True)

    completed_ids = set(
        HabitLog.objects.filter(date=today, completed=True).values_list(
            'habit_id', flat=True)
    )

    habit_data = [{'habit': h, 'done': h.id in completed_ids} for h in habits]

    total = habits.count()
    completed_count = len(completed_ids)
    percent = int((completed_count / total) * 100) if total else 0

    context = {
        'habit_data': habit_data,
        'today': today,
        'completed_count': completed_count,
        'total': total,
        'percent': percent,
    }
    return render(request, 'routines/today.html', context)


@require_POST
def toggle_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id)
    today = timezone.localdate()

    log, created = HabitLog.objects.get_or_create(
        habit=habit, date=today, defaults={'completed': True}
    )
    if not created:
        log.completed = not log.completed
        log.save()

    return redirect('routines:today')


def stats_view(request):
    period = request.GET.get('period', 'week')
    days = 30 if period == 'month' else 7

    today = timezone.localdate()
    start_date = today - timedelta(days=days - 1)
    date_list = [start_date + timedelta(days=i) for i in range(days)]

    habits = Habit.objects.filter(is_active=True)

    logs = HabitLog.objects.filter(
        date__gte=start_date, date__lte=today, completed=True)
    log_set = {(log.habit_id, log.date) for log in logs}

    habit_stats = []
    total_possible = 0
    total_completed = 0

    for h in habits:
        completed_days = sum(1 for d in date_list if (h.id, d) in log_set)
        missed_days = days - completed_days
        percent = int((completed_days / days) * 100) if days else 0

        habit_stats.append({
            'habit': h,
            'completed': completed_days,
            'missed': missed_days,
            'percent': percent,
        })
        total_possible += days
        total_completed += completed_days

    overall_percent = int((total_completed / total_possible)
                          * 100) if total_possible else 0

    grid = []
    for d in date_list:
        row = {
            'date': d,
            'is_today': d == today,
            'cells': [(h.id, d) in log_set for h in habits],
        }
        grid.append(row)

    context = {
        'period': period,
        'days': days,
        'habit_stats': habit_stats,
        'overall_percent': overall_percent,
        'total_completed': total_completed,
        'total_possible': total_possible,
        'total_missed': total_possible - total_completed,
        'habits': habits,
        'grid': grid,
        'start_date': start_date,
        'today': today,
    }
    return render(request, 'routines/stats.html', context)
