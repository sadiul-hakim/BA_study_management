from django.db import models


class Guide(models.Model):
    PRIMARY = 1
    WARNING = 2
    DANGER = 3

    TYPE = [
        (PRIMARY, "Primary"),
        (WARNING, "Warning"),
        (DANGER, "Danger"),
    ]

    text = models.TextField()
    priority = models.IntegerField(default=0)
    type = models.IntegerField(choices=TYPE, default=WARNING)

    class Meta:
        ordering = ['priority']

    def __str__(self):
        return f"Guide {self.priority}"

    def bootstrap_class(self):
        return {
            self.PRIMARY: "card-primary",
            self.WARNING: "card-warning",
            self.DANGER: "card-danger",
        }.get(self.type, "card-secondary")
