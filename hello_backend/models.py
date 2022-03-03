from django.contrib.auth.models import AbstractUser
from django.db import models

from common.model import BaseModel


class Workspace(BaseModel):
    name = models.CharField(max_length=125)
    creator_id = models.BigIntegerField(default=0)


class Board(BaseModel):
    name = models.CharField(max_length=125)
    creator_id = models.BigIntegerField()


class CardList(BaseModel):
    title = models.CharField(max_length=125)
    position = models.IntegerField()
    board_id = models.BigIntegerField()
    creator_id = models.BigIntegerField()
    sorted_by = models.CharField(max_length=50)
    num_card_limit = models.IntegerField()


class Card(BaseModel):
    title = models.CharField(max_length=125)
    position = models.IntegerField()
    slug = models.CharField(max_length=125)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    description = models.CharField(max_length=500)
    cover_url = models.CharField(max_length=125)
    card_list_id = models.BigIntegerField()
    creator_id = models.BigIntegerField()


class CardLabel(BaseModel):
    card_id = models.BigIntegerField()
    label_id = models.BigIntegerField()


class Label(BaseModel):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    workspace_id = models.IntegerField()
    creator_id = models.IntegerField()


class CardMember(BaseModel):
    card_id = models.BigIntegerField()
    user_id = models.BigIntegerField()


class WorkspaceMember(BaseModel):
    workspace_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
