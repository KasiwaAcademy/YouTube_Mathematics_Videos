from manim import *

class Thumbnail(Scene):
    def construct(self):
        # Add background image
        background = ImageMobject("../Image/chalk_board.jpg")
        background.set_z_index(-1)
        background.scale_to_fit_height(config.frame_height)
        background.scale_to_fit_width(config.frame_width)
        self.add(background)
        
        # Title text
        title = Text(
            "Deriving the", font="Roboto", weight=BOLD, color=YELLOW
        ).scale(1.5).to_edge(UP)

        subtitle = Text(
            "Quadratic Formula", font="Roboto", weight=BOLD, color=WHITE
        ).scale(1.5).next_to(title, DOWN, buff=0.3)

        # Quadratic Formula
        formula = MathTex(
            r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}", color=WHITE
        ).scale(1.7).next_to(subtitle, DOWN, buff=1)

        # Add everything
        self.add(title, subtitle, formula)