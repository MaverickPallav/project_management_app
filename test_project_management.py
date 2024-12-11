import unittest
from models import User, Board, List, Card
from views import ProjectManagementApp

class TestProjectManagementApp(unittest.TestCase):
    def setUp(self):
        self.app = ProjectManagementApp()
        self.user = User("John Doe", "john@example.com")
        self.board = self.app.create_board("Project A")
        self.list_ = self.app.create_list(self.board.boardId, "To Do")
        self.card = self.app.create_card(self.board.boardId, self.list_.listId, "Task 1", "Description of task")

    def test_create_board(self):
        self.assertEqual(self.board.name, "Project A")
        self.assertEqual(self.board.privacy, "PUBLIC")

    def test_create_list(self):
        self.assertEqual(self.list_.name, "To Do")
        self.assertEqual(len(self.list_.cards), 1)

    def test_create_card(self):
        self.assertEqual(self.card.name, "Task 1")
        self.assertEqual(self.card.description, "Description of task")
        self.assertIsNone(self.card.assigned_user)

    def test_assign_user_to_card(self):
        self.app.assign_user_to_card(self.board.boardId, self.list_.listId, self.card.cardId, self.user)
        self.assertEqual(self.card.assigned_user, self.user)

    def test_move_card(self):
        new_list = self.app.create_list(self.board.boardId, "In Progress")
        self.app.move_card(self.board.boardId, self.list_.listId, new_list.listId, self.card.cardId)
        self.assertEqual(len(self.list_.cards), 0)
        self.assertEqual(len(new_list.cards), 1)

    # New tests
    def test_clone_list(self):
        card2 = self.app.create_card(self.board.boardId, self.list_.listId, "Task 2", "Another task")
        cloned_list = self.list_.clone()
        self.assertEqual(len(cloned_list.cards), 2)
        self.assertNotEqual(cloned_list.cards[0].cardId, self.list_.cards[0].cardId)

    def test_clear_cards(self):
        self.app.delete_card(self.board.boardId, self.list_.listId, self.card.cardId)
        self.app.create_card(self.board.boardId, self.list_.listId, "New Task", "New task description")
        self.list_.clear_cards()
        self.assertEqual(len(self.list_.cards), 0)

    def test_add_tag_to_card(self):
        self.card.add_tag("Urgent")
        self.assertIn("Urgent", self.card.tags)

    def test_get_cards_by_tag(self):
        self.card.add_tag("Urgent")
        card2 = self.app.create_card(self.board.boardId, self.list_.listId, "Task 2", "Second task")
        card2.add_tag("Urgent")
        cards = self.app.get_cards_by_tag("Urgent")
        self.assertEqual(len(cards), 2)

    def test_get_cards_by_user(self):
        # Assign the user to both cards
        self.app.assign_user_to_card(self.board.boardId, self.list_.listId, self.card.cardId, self.user)
        card2 = self.app.create_card(self.board.boardId, self.list_.listId, "Task 2", "Second task")
        self.app.assign_user_to_card(self.board.boardId, self.list_.listId, card2.cardId, self.user)
        
        # Get all cards assigned to the user
        cards = self.app.get_cards_by_user(self.user)
        
        # Verify that the user has two cards assigned
        self.assertEqual(len(cards), 2)

if __name__ == '__main__':
    unittest.main()
