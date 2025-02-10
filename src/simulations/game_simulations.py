import pygame

from src.models.games.fotf_game import FotfGame

def run_fotf_game():
    fotf_game = FotfGame()
    # Solve for nxm Room of n and m Tiles
    # Solve for 2x2 Room Battle with 2 Prisms of 1 team
    # Solve for 4x4 Room Battle with 4 Prisms of 1 or 2 teams
    # Solve for 8x8 Room Battle with 8 Prisms of 1 or 2 or 4 teams
    # Solve for 9x9 Room Battle with 9 Prisms of 1 or 3 teams
    # Solve for 16x16 Room Battle with 12 Prisms of 1 or 2 or 3 or 4 or 6 or 8 or 9 or 12 teams
    # Solve for 64x64 Rooms of Land and Orbit Tile Spaces for 16 Prisms of 1 StarCruiser

def run_game_simulations():
    run_fotf_game()

def sample_checkers_game():
    # Initialize Pygame
    pygame.init()

    # Constants
    WIDTH, HEIGHT = 600, 600
    ROWS, COLS = 8, 8
    SQUARE_SIZE = WIDTH // COLS

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (200, 0, 0)
    GRAY = (160, 160, 160)

    # Pygame Setup
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Checkers Board")

    # Define Checkers Board Data
    def create_board():
        """Generates an 8x8 checkers board with initial pieces"""
        board = [["." for _ in range(COLS)] for _ in range(ROWS)]

        # Place pieces in initial positions
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 1:  # Pieces only on dark squares
                    if row < 3:
                        board[row][col] = "B"  # Black pieces
                    elif row > 4:
                        board[row][col] = "W"  # White pieces
        return board

    # Draw Board
    def draw_board(board):
        screen.fill(WHITE)  # Fill background

        for row in range(ROWS):
            for col in range(COLS):
                color = GRAY if (row + col) % 2 == 1 else WHITE
                pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

                # Draw pieces
                piece = board[row][col]
                if piece != ".":
                    piece_color = BLACK if piece == "B" else RED
                    pygame.draw.circle(
                        screen, piece_color,
                        (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                        SQUARE_SIZE // 3
                    )

    # Game Loop
    board = create_board()
    running = True

    while running:
        draw_board(board)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    run_fotf_game()
    print("debug finished")
