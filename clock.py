import tkinter as tk
import datetime
import math
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CENTER_X = CANVAS_WIDTH // 2
CENTER_Y = CANVAS_HEIGHT // 2
CLOCK_RADIUS = 150

HOUR_HAND_LENGTH = CLOCK_RADIUS * 0.5
MINUTE_HAND_LENGTH = CLOCK_RADIUS * 0.7
SECOND_HAND_LENGTH = CLOCK_RADIUS * 0.85

HOUR_HAND_WIDTH = 6
MINUTE_HAND_WIDTH = 4
SECOND_HAND_WIDTH = 2


def draw_hand(canvas, center_x, center_y, length, angle_deg, hand_tag, color, width):
    angle_rad = math.radians(angle_deg)
    end_x = center_x + length * math.sin(angle_rad)
    end_y = center_y - length * math.cos(angle_rad)

    canvas.create_line(center_x, center_y, end_x, end_y,
                       fill=color, width=width, tags=hand_tag)

def update_clock(canvas, root):
    now = datetime.datetime.now().time()
    hours = now.hour
    minutes = now.minute
    seconds = now.second

    second_angle = (seconds) * 6
    minute_angle = (minutes + seconds / 60.0) * 6
    hour_angle = (hours % 12 + minutes / 60.0 + seconds / 3600.0) * 30

    canvas.delete("hands")


    draw_hand(canvas, CENTER_X, CENTER_Y, HOUR_HAND_LENGTH, hour_angle, "hands", "black", HOUR_HAND_WIDTH)
    draw_hand(canvas, CENTER_X, CENTER_Y, MINUTE_HAND_LENGTH, minute_angle, "hands", "blue", MINUTE_HAND_WIDTH)
    draw_hand(canvas, CENTER_X, CENTER_Y, SECOND_HAND_LENGTH, second_angle, "hands", "red", SECOND_HAND_WIDTH)


    root.after(1000, update_clock, canvas, root)

def draw_clock_face(canvas):
    canvas.create_oval(CENTER_X - CLOCK_RADIUS, CENTER_Y - CLOCK_RADIUS,
                       CENTER_X + CLOCK_RADIUS, CENTER_Y + CLOCK_RADIUS,
                       outline="black", width=2)

    canvas.create_oval(CENTER_X - 5, CENTER_Y - 5, CENTER_X + 5, CENTER_Y + 5, fill="black")

    for i in range(12):
        angle_deg = i * 30
        angle_rad = math.radians(angle_deg)

        mark_start_x = CENTER_X + (CLOCK_RADIUS - 15) * math.sin(angle_rad)
        mark_start_y = CENTER_Y - (CLOCK_RADIUS - 15) * math.cos(angle_rad)
        mark_end_x = CENTER_X + CLOCK_RADIUS * math.sin(angle_rad)
        mark_end_y = CENTER_Y - CLOCK_RADIUS * math.cos(angle_rad)

        mark_width = 3 if i % 3 == 0 else 1

        canvas.create_line(mark_start_x, mark_start_y, mark_end_x, mark_end_y,
                           width=mark_width, fill="black")

        if i == 0:
             text_angle_deg = 0
             text_radius = CLOCK_RADIUS - 30
             text_x = CENTER_X + text_radius * math.sin(math.radians(text_angle_deg))
             text_y = CENTER_Y - text_radius * math.cos(math.radians(text_angle_deg))
             canvas.create_text(text_x, text_y, text="12", font=("Arial", 12, "bold"))
        elif i == 3:
             text_angle_deg = 90
             text_radius = CLOCK_RADIUS - 30
             text_x = CENTER_X + text_radius * math.sin(math.radians(text_angle_deg))
             text_y = CENTER_Y - text_radius * math.cos(math.radians(text_angle_deg))
             canvas.create_text(text_x, text_y, text="3", font=("Arial", 12, "bold"))
        elif i == 6:
             text_angle_deg = 180
             text_radius = CLOCK_RADIUS - 30
             text_x = CENTER_X + text_radius * math.sin(math.radians(text_angle_deg))
             text_y = CENTER_Y - text_radius * math.cos(math.radians(text_angle_deg))
             canvas.create_text(text_x, text_y, text="6", font=("Arial", 12, "bold"))
        elif i == 9:
             text_angle_deg = 270
             text_radius = CLOCK_RADIUS - 30
             text_x = CENTER_X + text_radius * math.sin(math.radians(text_angle_deg))
             text_y = CENTER_Y - text_radius * math.cos(math.radians(text_angle_deg))
             canvas.create_text(text_x, text_y, text="9", font=("Arial", 12, "bold"))


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Аналоговые часы")

    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
    canvas.pack(pady=20)

    draw_clock_face(canvas)

    update_clock(canvas, root)

    root.mainloop()
