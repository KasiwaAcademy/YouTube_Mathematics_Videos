# figure_creator.py
from manim import *
import numpy as np

def create_geometric_figure(radius=3, origin=ORIGIN):
    """
    Creates a geometric figure consisting of a circle, two triangles,
    labeled points, an angle, and equality tick marks.

    Args:
        radius (float): The radius of the main circle.
        origin (np.ndarray): The center point (x, y, z) of the circle.

    Returns:
        dict: A dictionary of VGroups, organized by element type 
              for easy animation. Keys are:
              "main_shapes", "points_and_labels", "annotations".
    """
    
    # --- 1. Define Angles and Points ---
    # Angles are defined in degrees and converted to radians for calculation.
    # Point D
    angle_d_deg = 20
    point_D = Circle(radius=radius, color=BLACK).move_to(origin).point_at_angle(angle_d_deg * DEGREES)
    
    # Point A is diametrically opposite to D
    point_A = origin - (point_D - origin)

    # Point B
    angle_b_deg = 110
    point_B = Circle(radius=radius, color=BLACK).move_to(origin).point_at_angle(angle_b_deg * DEGREES)
    
    # Point C
    angle_c_deg = 65
    point_C = Circle(radius=radius, color=BLACK).move_to(origin).point_at_angle(angle_c_deg * DEGREES)

    # --- 2. Create Main Geometric Shapes ---
    circle = Circle(radius=radius, color=WHITE, stroke_width=2).move_to(origin)
    triangle_1 = Polygon(point_A, point_B, point_D, color=WHITE, stroke_width=2)
    triangle_2 = Polygon(point_B, point_C, point_D, color=WHITE, stroke_width=2)
    
    main_shapes = VGroup(circle, triangle_1, triangle_2)

    # --- 3. Create Dots and Labels for each Point ---
    dot_A = Dot(point_A, color=WHITE, radius=0.04)
    label_A = Text("A", font_size=24).next_to(dot_A, direction=LEFT)

    dot_B = Dot(point_B, color=WHITE, radius=0.04)
    label_B = Text("B", font_size=24).next_to(dot_B, direction=UP)

    dot_C = Dot(point_C, color=WHITE, radius=0.04)
    label_C = Text("C", font_size=24).next_to(dot_C, direction=RIGHT)

    dot_D = Dot(point_D, color=WHITE, radius=0.04)
    label_D = Text("D", font_size=24).next_to(dot_D, direction=RIGHT)
    
    dot_O = Dot(origin, color=WHITE, radius=0.04)
    label_O = Text("O", font_size=24).next_to(dot_O, direction=DOWN)

    points_and_labels = VGroup(
        dot_A, label_A, dot_B, label_B, dot_C, label_C, dot_D, label_D, dot_O, label_O
    )

    # --- 4. Create Annotations (Angle and Tick Marks) ---
    # Angle at vertex A
    angle_at_A = Angle(Line(point_A, point_B), Line(point_A, point_D), radius=0.5, color=WHITE, stroke_width=2, other_angle = True)
    angle_label = MathTex(r"52^\circ").scale(0.7).next_to(point_A, UP + RIGHT, buff = 0.5)

    # Tick marks to indicate BC = DC
    def create_tick_mark(p1, p2, tick_length=0.2):
        """Helper function to create a single tick mark on a line segment."""
        line_vec = p2 - p1
        line_dir = line_vec / np.linalg.norm(line_vec)
        perp_dir = np.array([-line_dir[1], line_dir[0], 0]) # Perpendicular in XY plane
        midpoint = (p1 + p2) / 2
        tick = Line(
            midpoint - perp_dir * tick_length / 2,
            midpoint + perp_dir * tick_length / 2,
            color=WHITE, stroke_width=2
        )
        return tick

    tick_BC = create_tick_mark(point_B, point_C)
    tick_DC = create_tick_mark(point_D, point_C)
    
    annotations = VGroup(angle_at_A, angle_label, tick_BC, tick_DC)

    # --- 5. Return all parts in a dictionary ---
    return {
        "main_shapes": main_shapes,
        "points_and_labels": points_and_labels,
        "annotations": annotations
    }
