from models import Board, List, Card, User

class ProjectManagementApp:
    def __init__(self):
        self.boards = {}

    def create_board(self, name, privacy="PUBLIC"):
        board = Board(name, privacy)
        self.boards[board.boardId] = board
        return board

    def delete_board(self, board_id):
        if board_id in self.boards:
            del self.boards[board_id]

    def create_list(self, board_id, list_name):
        board = self.boards.get(board_id)
        if board:
            list_ = List(list_name)
            board.add_list(list_)
            return list_

    def delete_list(self, board_id, list_id):
        board = self.boards.get(board_id)
        if board:
            board.remove_list(list_id)

    def create_card(self, board_id, list_id, name, description):
        board = self.boards.get(board_id)
        if board:
            list_ = next((lst for lst in board.lists if lst.listId == list_id), None)
            if list_:
                card = Card(name, description)
                list_.add_card(card)
                return card

    def delete_card(self, board_id, list_id, card_id):
        board = self.boards.get(board_id)
        if board:
            list_ = next((lst for lst in board.lists if lst.listId == list_id), None)
            if list_:
                list_.remove_card(card_id)

    def assign_user_to_card(self, board_id, list_id, card_id, user):
        board = self.boards.get(board_id)
        if board:
            list_ = next((lst for lst in board.lists if lst.listId == list_id), None)
            if list_:
                card = next((c for c in list_.cards if c.cardId == card_id), None)
                if card:
                    card.assigned_user = user

    def unassign_user_from_card(self, board_id, list_id, card_id):
        board = self.boards.get(board_id)
        if board:
            list_ = next((lst for lst in board.lists if lst.listId == list_id), None)
            if list_:
                card = next((c for c in list_.cards if c.cardId == card_id), None)
                if card:
                    card.assigned_user = None

    def move_card(self, board_id, from_list_id, to_list_id, card_id):
        board = self.boards.get(board_id)
        if board:
            from_list = next((lst for lst in board.lists if lst.listId == from_list_id), None)
            to_list = next((lst for lst in board.lists if lst.listId == to_list_id), None)
            if from_list and to_list:
                card = next((c for c in from_list.cards if c.cardId == card_id), None)
                if card:
                    from_list.remove_card(card_id)
                    to_list.add_card(card)

    def get_cards_by_tag(self, tag):
        cards_with_tag = []
        for board in self.boards.values():
            for list_ in board.lists:
                for card in list_.cards:
                    if tag in card.tags:
                        cards_with_tag.append(card)
        return cards_with_tag

    def get_cards_by_user(self, user):
        cards = []
        for board in self.boards.values():
            for list_ in board.lists:
                for card in list_.cards:
                    if card.assigned_user == user:
                        cards.append(card)
        return cards

    def add_member(self, board_id, user):
        board = self.boards.get(board_id)
        if board:
            board.add_member(user)
