# Import the Libraries
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

# Make Configurations
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30
config.disable_caching = True

# Initialize a Scene
class QuadraticEquation(VoiceoverScene):
    def construct(self):
        # Set Up speech services
        self.set_speech_service(GTTSService(lang="en"))

        # Add background image
        background = ImageMobject("../../Image/chalk_board.jpg")
        background.set_z_index(-1)
        background.scale_to_fit_height(config.frame_height)
        background.scale_to_fit_width(config.frame_width)
        self.add(background)

        # Load and position logo image
        logo = ImageMobject("../../Image/logo.png")
        logo_corner = logo.scale(0.15)
        logo_corner.to_corner(DR)
        self.add(logo_corner)

        # Intro
        text_1 = """
                Hello, welcome to yet another lesson on solving quadratic equestions here at Kasiwa \
                Academy. Please stay with us as we continue helping each other grow Mathematical skills.
                 """
        with self.voiceover(text_1) as tracker:
            title = Tex(r"Solving Quadratic Equations", color=YELLOW)
            institution = Tex(r"@Kasiwa Academy")
            self.play(Write(title))
            self.wait()
            self.play(title.animate.shift(UP).scale(1.5).set_color(WHITE), FadeIn(institution, shift=UP))
            self.wait()

        # Slide 1
        text_2 = """
                Let us begin by introducing our problem that we will solve. We are given a quadratic equation \
                3x² + 6x \N{MINUS SIGN} 2 = 0. We are asked to solve the equation giving the final answer correct to three significant figures. 
                 """
        with self.voiceover(text_2) as tracker:
            sub_title_1 = Tex(r"Problem Statement :", color=YELLOW)
            statement_1 = Tex(r"Solve the equation $3x^2 + 6x - 2 = 0$, giving the answer\\"
                              r"correct to three significant figures.")
            self.play(FadeOut(title, institution, shift=UP), Write(sub_title_1))
            self.wait()
            self.play(sub_title_1.animate.to_edge(UP).scale(1.5).set_color(WHITE), FadeIn(statement_1, shift=UP))
            self.wait()
            self.play(statement_1.animate.scale(1.1))
        self.wait()

        # Slide 2
        text_3 = """
                Let us get started by isolating the given equation from the problem statement.
                 """
        with self.voiceover(text_3) as tracker:
            sub_title_2 = Tex(r"Start with the given equation :", color=YELLOW).shift(2*DOWN)
            eq1 = MathTex(r"3x^2 + 6x - 2 = 0")
            self.play(Write(sub_title_2))
            self.wait()
            self.play(FadeOut(sub_title_1, statement_1, shift=UP), sub_title_2.animate.to_edge(UP).set_color(WHITE).scale(1.5),
                     Write(eq1))
            self.wait()
            self.play(eq1.animate.scale(1.5))
        self.wait()

        # Slide 3
        text_4 = """
                We will use the quadratic formula which is derived from the standard quadratic equation\
                ax² + bx + c = 0 where a \N{NOT EQUAL TO} 0. Comparing the given equation to this form, we find that\
                a=3, b=6 and c=\N{MINUS SIGN}2.
                 """
        with self.voiceover(text_4) as tracker:
            sub_title_3 = Tex(r"Use the quadratic formula :", color=YELLOW).shift(2*DOWN)
            statement_2 = Tex(r"Where: $a$ = $3$, $b$ = $6$, and $c$ = $-2$").move_to([0, 1, 0]).scale(1.3)
            formula = MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}").move_to([0, -1, 0]).scale(1.3)
            self.play(Write(sub_title_3))
            self.wait()
            self.play(FadeOut(sub_title_2, shift=UP), eq1.animate.move_to([0, 2.5, 0]), FadeIn(statement_2, formula, shift=UP),
                     sub_title_3.animate.to_edge(UP).set_color(WHITE).scale(1.3))
        self.wait()

        # Slide 4
        text_5 = """
                Next, substitute a with 3, b with 6, and c with −2 in the quadratic formula, then solve for x.
                 """
        with self.voiceover(text_5) as tracker:
            eq2 = MathTex(r"x = \frac{-(6) \pm \sqrt{(6)^2 - 4(3)(-2)}}{2(3)}").move_to([0, -2, 0]).scale(1.3)
            self.play(FadeOut(eq1, shift=UP), statement_2.animate.move_to([0, 2.3, 0]),
                     formula.animate.move_to([0, 0.7, 0]))
            self.wait()
            self.play(TransformFromCopy(formula, eq2))
        self.wait()

        # Slide 5
        text_5 = """
                Continue by simplifying the right hand side of the formula.
                 """
        with self.voiceover(text_5) as tracker:
            eq3 = MathTex(r"x = \frac{-6 \pm \sqrt{36 + 24}}{6}").scale(1.2)
            eq4 = MathTex(r"x = \frac{-6 \pm \sqrt{60}}{6}").move_to([-3, -1.8, 0]).scale(1.2)
            eq5 = MathTex(r"x = \frac{-6 \pm \sqrt{7.746}}{6}").move_to([3, -1.8, 0]).scale(1.2)
            self.play(FadeOut(statement_2, formula, shift=UP), eq2.animate.move_to([0, 2, 0]))
            self.wait()
            self.play(TransformFromCopy(eq2, eq3))
            self.wait()
            self.play(TransformFromCopy(eq3, eq4))
            self.wait()
            self.play(TransformFromCopy(eq4, eq5))
        self.wait()

        # Slide 6
        text_6 = """
                Solve for each value of x. A quadratic equation typically has two solutions, unless otherwise.
                 """
        with self.voiceover(text_6) as tracker:
            sub_title_4 = Tex(r"Solve for each value of $x$ :", color=YELLOW).to_edge(DOWN)
            eq6 = MathTex(r"x = \frac{-6 + 7.746}{6}").scale(1.2).move_to([-3, 0, 0])
            eq7 = MathTex(r"x = \frac{-6 - 7.746}{6}").scale(1.2).move_to([3, 0, 0])
            eq8 = MathTex(r"x = 0.291").scale(1.2).move_to([-3, -1.5, 0])
            eq9 = MathTex(r"x = -2.291").scale(1.2).move_to([3, -1.5, 0])
            self.play(Write(sub_title_4))
            self.play(FadeOut(sub_title_3, eq2, eq3, eq4, shift=UP), sub_title_4.animate.to_edge(UP).scale(1.5).set_color(WHITE),
                     eq5.animate.move_to([0, 2, 0]))
            self.wait()
            self.play(TransformFromCopy(eq5, eq6), TransformFromCopy(eq5, eq7))
            self.wait()
            self.play(TransformFromCopy(eq6, eq8), TransformFromCopy(eq7, eq9))
        self.wait()

        # Slide 7
        text_7 = """
                We are asked to give the final answers correct to 3 significant figures.
                 """
        with self.voiceover(text_7) as tracker:
            sub_title_5 = Tex(r"Answers correct to 3 significant figures :", color=YELLOW).to_edge(DOWN)
            sub_title_6 = Tex(r"Final Answer:", color=YELLOW).to_edge(UP).scale(1.5)
            statement_3 = Tex(r"or").scale(1.2)
            eq10 = MathTex(r"x = 0.291").move_to([-3, 0, 0]).scale(1.2)
            eq11 = MathTex(r"x = -2.29").move_to([3, 0, 0]).scale(1.2)
            self.play(Write(sub_title_5))
            self.wait()
            self.play(FadeOut(sub_title_4, eq5, eq6, eq7, shift=UP), eq8.animate.move_to([-3, 2, 0]),
                     eq9.animate.move_to([3, 2, 0]), sub_title_5.animate.to_edge(UP))
            self.wait()
            self.play(TransformFromCopy(eq8, eq10), TransformFromCopy(eq9, eq11))
            self.wait()
            self.play(eq10.animate.scale(1.5).set_color(YELLOW), eq11.animate.scale(1.5).set_color(YELLOW), 
                      FadeIn(statement_3, shift=UP), FadeTransform(sub_title_5, sub_title_6), 
                      FadeOut(eq8, shift=LEFT), FadeOut(eq9, shift=RIGHT))
            self.play(Circumscribe(eq10), Circumscribe(eq11), )
            self.wait(3)
            shrink_group = VGroup(sub_title_6, eq10, eq11, statement_3)
            self.play(ShrinkToCenter(shrink_group))
        self.wait()
        
        # Outro
        outro_text = """
                    Thank you for watching.
                     """
        with self.voiceover(outro_text) as tracker:
            final_text = Tex("Thank you for watching!", color=YELLOW).scale(1.5)
            self.play(Write(final_text))
            self.wait()
            self.play(logo_corner.animate.move_to(ORIGIN).scale(3), 
                      final_text.animate.to_edge(DOWN).set_color(WHITE))
            self.wait(2)
            self.play(FadeOut(final_text, logo_corner))
        self.wait()