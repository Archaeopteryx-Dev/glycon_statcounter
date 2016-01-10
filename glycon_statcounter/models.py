from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

from glycon.models import BaseBlock
from .views import statcounter_block_html


class StatcounterBlock(BaseBlock):
    project_id = models.CharField(max_length=60)

    @property
    def content(self):
        return statcounter_block_html(self.project_id)

    def __str__(self):
        return self.name

    class Data:
        description = "Collect statistics for Statcounter"