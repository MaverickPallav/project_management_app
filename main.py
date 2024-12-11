from views import ProjectManagementApp
from models import User

def main():
    # Create an instance of the ProjectManagementApp
    app = ProjectManagementApp()

    # Create users
    user1 = User("Alice", "alice@example.com")
    user2 = User("Bob", "bob@example.com")

    # Create a board
    board = app.create_board("Project 1")
    print(f"Board Created: {board.name}, URL: {board.url}")

    # Add members to the board
    app.add_member(board.boardId, user1)
    app.add_member(board.boardId, user2)

    # Create a list within the board
    todo_list = app.create_list(board.boardId, "To Do")
    print(f"List Created: {todo_list.name}")

    # Create a card and assign a user
    card1 = app.create_card(board.boardId, todo_list.listId, "Task 1", "Complete the task description")
    app.assign_user_to_card(board.boardId, todo_list.listId, card1.cardId, user1)
    print(f"Card Created: {card1.name}, Assigned to: {card1.assigned_user.name}")

    # Demonstrating move card functionality
    in_progress_list = app.create_list(board.boardId, "In Progress")
    app.move_card(board.boardId, todo_list.listId, in_progress_list.listId, card1.cardId)
    print(f"Card Moved to: {in_progress_list.name}")

    # Demonstrate cloning a list
    cloned_list = todo_list.clone()
    print(f"Cloned List: {cloned_list.name}, Cards in cloned list: {len(cloned_list.cards)}")

    # Show all boards
    print("\nAll Boards:")
    for b in app.boards.values():
        print(f"- {b.name} (Privacy: {b.privacy})")

if __name__ == "__main__":
    main()
