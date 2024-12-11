import uuid

class User:
    def __init__(self, name, email):
        self.userId = uuid.uuid4()
        self.name = name
        self.email = email

class Card:
    def __init__(self, name, description):
        self.cardId = uuid.uuid4()
        self.name = name
        self.description = description
        self.assigned_user = None
        self.tags = []

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)

class List:
    def __init__(self, name):
        self.listId = uuid.uuid4()
        self.name = name
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card_id):
        self.cards = [card for card in self.cards if card.cardId != card_id]

    def clear_cards(self):
        self.cards = []

    def clone(self):
        cloned_list = List(f"Cloned {self.name}")
        for card in self.cards:
            cloned_card = Card(card.name, card.description)
            cloned_list.add_card(cloned_card)
        return cloned_list

class Board:
    def __init__(self, name, privacy="PUBLIC"):
        self.boardId = uuid.uuid4()
        self.name = name
        self.privacy = privacy
        self.url = f"/board/{self.boardId}"
        self.lists = []
        self.members = []

    def add_list(self, list_):
        self.lists.append(list_)

    def remove_list(self, list_id):
        self.lists = [list_ for list_ in self.lists if list_.listId != list_id]

    def add_member(self, user):
        if user not in self.members:
            self.members.append(user)

    def remove_member(self, user):
        self.members = [member for member in self.members if member.userId != user.userId]
