import pygame
import sys

def interpret_line(line):
    if line.strip() == "":
        return "noop"
    elif line.startswith(" "):
        return "append"
    return "new"

def read_from_stdin():
    # Process the lines to group intentions
    intention_list = []
    current_intention = ""
    
    for line in sys.stdin:
        match interpret_line(line):
            case "new":
                if current_intention:
                    intention_list.append(current_intention)
                current_intention = line
            case "append":
                current_intention += "\n" + line
    if current_intention:  # Add the last intention if any
        intention_list.append(current_intention)

    return intention_list

def wrap_text(text, font, max_width):
    """Wrap the text to fit within the specified width."""
    words = text.split(' ')
    lines = []
    current_line = words[0]
    for word in words[1:]:
        test_line = current_line + " " + word
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)
    return lines

def main():
    data = read_from_stdin()
    print(data)

    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Seminario")
    font = pygame.font.SysFont(None, 40)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    index = 0

    def display_text(text):
        screen.fill(WHITE)

        # Split the text into lines and determine the indentation level for each line.
        original_lines = text.split("\n")
        indents = [len(line) - len(line.lstrip()) for line in original_lines]

        # Calculate indentation width. This might need adjusting.
        indent_width = font.size("    ")[0]

        # Determine the maximum width allowed for wrapped text.
        max_content_width = screen.get_width() - 2*indent_width

        # Handle wrapping and render each line.
        lines = []
        for i, line in enumerate(original_lines):
            wrapped_lines = wrap_text(line.lstrip(), font, max_content_width - indents[i] * indent_width)
            for wrapped_line in wrapped_lines:
                lines.append((indents[i], wrapped_line))

        rendered_lines = [font.render(line[1], True, BLACK) for line in lines]

        # Determine the height of the container.
        total_height = sum([rt.get_height() for rt in rendered_lines])

        # Calculate the starting position of the container.
        start_x = (screen.get_width() - max_content_width) / 2
        start_y = (screen.get_height() - total_height) / 2

        for i, rendered_text in enumerate(rendered_lines):
            screen.blit(rendered_text, (start_x + lines[i][0] * indent_width, start_y))
            start_y += rendered_text.get_height()

        pygame.display.flip()

    running = True
    display_text('Presiona espacio para comenzar.')

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                if event.key == pygame.K_SPACE:
                    if index < len(data):
                        display_text(data[index])
                        index += 1
                    else:
                        display_text("Fin del seminario.")
                        pygame.time.wait(2000)
                        running = False

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
