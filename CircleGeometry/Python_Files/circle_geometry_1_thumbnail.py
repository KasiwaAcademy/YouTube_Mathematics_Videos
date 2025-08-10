from manim import *

class Thumbnail(Scene):
    def construct(self):
        # Add background image
        background = ImageMobject("../Image/chalk_board.jpg")
        background.set_z_index(-1)
        background.scale_to_fit_height(config.frame_height)
        background.scale_to_fit_width(config.frame_width)
        self.add(background)

        # Color Configurations
        main_color = BLUE_A
        accent_color = YELLOW
        secondary_color = GREEN
        text_color = WHITE
        
        # Title text
        title = Text(
            "Solving", font="Roboto", weight=BOLD, color=YELLOW
        ).scale(1.5).to_edge(UP)

        subtitle = Text(
            "Circle Geometry Problem", font="Roboto", weight=BOLD, color=WHITE
        ).scale(1.5).next_to(title, DOWN, buff=0.3)
        
        ## Create the diagram
        circle = Circle(radius=1.75, color=main_color, stroke_width=2).shift(DOWN)
        center_O = Dot(circle.get_center(), color=text_color)
        O_label = Tex("O", color=text_color).scale(0.75).next_to(center_O, DOWN, buff=0.1)

        ## Points on the circle
        A = circle.point_at_angle(195 * DEGREES)
        D = circle.point_at_angle(15 * DEGREES)
        B = circle.point_at_angle(95 * DEGREES)
        C = circle.point_at_angle(55 * DEGREES)

        ## Create labels for points
        A_label = Tex("A", color=text_color).next_to(A, LEFT).scale(0.75)
        B_label = Tex("B", color=text_color).next_to(B, UP).scale(0.75)
        C_label = Tex("C", color=text_color).next_to(C, UP).scale(0.75)
        D_label = Tex("D", color=text_color).next_to(D, RIGHT).scale(0.75)
        labels = VGroup(A_label, B_label, C_label, D_label)

        ## Create chords and diagonals
        AD = Line(A, D, color=main_color, stroke_width=2)
        AB = Line(A, B, color=main_color, stroke_width=2)
        BC = Line(B, C, color=main_color, stroke_width=2)
        CD = Line(C, D, color=main_color, stroke_width=2)
        BD = Line(B, D, color=main_color, stroke_width=2)
        AC = DashedLine(A, C, color=accent_color, stroke_width=2)

        ## Highlight given info
        angle_DAB = Angle(Line(A,D), Line(A,B), radius=0.7, color=text_color, stroke_width=2)
        angle_DAB_label = Tex(r"52$^\circ$", color=text_color).scale(0.7).next_to(A, UP+RIGHT, buff=0.75).shift(DOWN*0.2)
        tick_BC = Line(BC.get_center() + 0.1*rotate_vector(BC.get_unit_vector(), PI/2), BC.get_center() - 0.1*rotate_vector(BC.get_unit_vector(), PI/2), color=text_color, stroke_width=2)
        tick_CD = Line(CD.get_center() + 0.1*rotate_vector(CD.get_unit_vector(), PI/2), CD.get_center() - 0.1*rotate_vector(CD.get_unit_vector(), PI/2), color=text_color,stroke_width=2)

        circle_group = VGroup(circle, AD, center_O, O_label, AB, BC, CD, BD, labels,
                         angle_DAB, angle_DAB_label, tick_BC, tick_CD)
        

        # Add everything
        self.add(title, subtitle, circle_group)