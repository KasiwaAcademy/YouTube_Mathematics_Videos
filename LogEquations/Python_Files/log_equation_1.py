from manim import *

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30

class SolveLogEquation(Scene):
    def construct(self):
        # Add background image
        background = ImageMobject("../Image/chalk_board.jpg")
        background.set_z_index(-1)
        background.scale_to_fit_height(config.frame_height)
        background.scale_to_fit_width(config.frame_width)
        self.add(background)

         # Load and position logo image
        logo = ImageMobject("../Image/logo.png")
        logo_corner = logo.scale(0.15)
        logo_corner.to_corner(DR)
        self.add(logo_corner)

        # Intro
        title = Tex(r"Solving Logarithmic Equation", color=YELLOW)
        sub_title = Tex(r"@Kasiwa Academy")
        intro_group = VGroup(title, sub_title)
        self.play(Write(title))
        self.wait()
        self.play(title.animate.shift(UP).scale(1.75).set_color(WHITE))
        self.wait()
        self.play(FadeIn(sub_title))
        self.wait(2)
        
        # Title
        text = Tex(r"Problem Statement:", color=YELLOW)
        statement = Tex(r"Solve the equation $2\log y = \log(3y + 4)$")
        title_group = VGroup(text, statement)
        self.play(Write(text), FadeOut(intro_group, shift=RIGHT))
        self.wait()
        self.play(text.animate.to_edge(UP).scale(1.75).set_color(WHITE))
        self.wait()
        self.play(FadeIn(statement))
        self.wait()
        self.play(statement.animate.shift(UP).scale(1.5))
        self.wait(3)

        # Step 1: Original equation
        eq1 = MathTex(r"2\log y = \log(3y + 4)")
        note1 = Tex("Start with the given equation:", color=YELLOW)
        self.play(Write(note1), FadeOut(title_group))
        self.wait()
        self.play(note1.animate.to_edge(UP).scale(1.75).set_color(WHITE))
        self.wait()
        self.play(Write(eq1))
        self.wait()
        self.play(eq1.animate.scale(1.5))
        self.wait(3)

        # Step 2: Apply power rule
        eq2 = MathTex(r"\log(y^2) = \log(3y + 4)").shift(DOWN).scale(1.5)
        note2 = Tex(r"Use: $a\log b = \log(b^a)$", color=YELLOW).shift(DOWN)
        self.play(Write(note2))
        self.wait(3)
        self.play(FadeOut(note1, shift=UP), note2.animate.to_edge(UP).set_color(WHITE).scale(1.75),
                 eq1.animate.shift(UP))
        self.wait()
        self.play(TransformFromCopy(eq1, eq2))
        self.wait(3)

        # Step 3: Expand the right handside
        note3 = Tex(r"Expand the right handside:", color=YELLOW).shift(2*DOWN)
        eq3 = MathTex(r"\log(y^2) = \log(3y) + \log4").shift(DOWN).scale(1.5)
        self.play(Write(note3))
        self.wait()
        self.play(FadeOut(note2, eq1, shift=UP), note3.animate.to_edge(UP).set_color(WHITE).scale(1.75),
                 eq2.animate.shift(2*UP))
        self.wait()
        self.play(TransformFromCopy(eq2, eq3))
        self.wait(3)
        
        # Step 4: Remove logs
        eq4 = MathTex("y^2 = 3y + 4").shift(DOWN).scale(1.5)
        note4 = Tex("Equal logs → equal arguments", color=YELLOW).shift(2*DOWN)
        self.play(Write(note4))
        self.wait()
        self.play(FadeOut(note3, eq2), note4.animate.to_edge(UP).set_color(WHITE).scale(1.75),
                 eq3.animate.shift(2*UP))
        self.wait()
        self.play(TransformFromCopy(eq3, eq4))
        self.wait(3)

        # Step 4: Rearranged quadratic form
        eq5 = MathTex("y^2 - 3y - 4 = 0").shift(DOWN).scale(1.5)
        note5 = Tex("Move all terms to one side:", color=YELLOW).shift(2*DOWN)
        self.play(Write(note5))
        self.wait()
        self.play(FadeOut(note4, eq3, shift=UP), note5.animate.to_edge(UP).set_color(WHITE).scale(1.75),
                 eq4.animate.shift(2*UP))
        self.wait()
        self.play(TransformFromCopy(eq4, eq5))
        self.wait(3)

        # Step 5: Quadratic formula
        formula = MathTex(r"y = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}").scale(1.5)
        eq6 = MathTex(r"y = \frac{-(-3) \pm \sqrt{(-3)^2 - 4(1)(-4)}}{2(1)}").scale(1.5).shift(1.5*DOWN)
        note6 = Tex("Use quadratic formula:", color=YELLOW).shift(2*DOWN)
        note_6 = Tex(r"where: $a = 1$, $b = -3$ and $c = -4$", color=YELLOW).shift(2*DOWN)
        self.play(Write(note6))
        self.wait()
        self.play(FadeOut(note5, eq4, shift=UP), note6.animate.to_edge(UP).set_color(WHITE).scale(1.75),
                 eq5.animate.shift(3*UP))
        self.wait()
        self.play(FadeIn(formula))
        self.wait()
        self.play(Write(note_6))
        self.wait()
        self.play(FadeOut(eq5, shift=UP), note_6.animate.shift(4.5*UP).scale(1.3).set_color(WHITE),
                 formula.animate.shift(UP))
        self.wait()
        self.play(TransformFromCopy(formula, eq6))
        self.wait(3)

        # Step 6: Simplify step by step
        eq7 = MathTex(r"y = \frac{3 \pm \sqrt{9 + 16}}{2}").scale(1.5)
        self.play(FadeOut(note6, note_6, formula, shift=UP), eq6.animate.to_edge(UP))
        self.wait()
        self.play(TransformFromCopy(eq6, eq7))
        self.wait(3)

        eq8 = MathTex(r"y = \frac{3 \pm \sqrt{25}}{2}").scale(1.5).shift(2*DOWN)
        self.play(TransformFromCopy(eq7, eq8))
        self.wait(3)

        eq9 = MathTex(r"y = \frac{3 \pm 5}{2}").scale(1.5).shift(DOWN)
        self.play(FadeOut(eq6, eq7, shift=UP), eq8.animate.shift(4*UP))
        self.wait()
        self.play(TransformFromCopy(eq8, eq9))
        self.wait(3)

        # Step 7: Show both possible answers
        answers_1 = MathTex(r"y = \frac{3 + 5}{2} \quad \text{or} \quad y = \frac{3 - 5}{2}").scale(1.5).shift(DOWN)
        answers_2 = MathTex(r"y = \frac{8}{2} \quad \text{or} \quad y = \frac{-2}{2}").scale(1.5).shift(0.5*UP)
        answers_3 = MathTex(r"y = 4 \quad \text{or} \quad y = -1").scale(1.5).shift(1.5*DOWN)
        note7 = Tex("Solve for both possibilities:", color=YELLOW).shift(3*DOWN)
        self.play(Write(note7))
        self.wait()
        self.play(FadeOut(eq8, shift=UP), eq9.animate.shift(2*UP), 
                  note7.animate.to_edge(UP).scale(1.75).set_color(WHITE))
        self.wait()
        self.play(TransformFromCopy(eq9, answers_1))
        self.wait()
        self.play(FadeOut(note7, eq9, shift=UP), answers_1.animate.to_edge(UP))
        self.wait()
        self.play(TransformFromCopy(answers_1, answers_2))
        self.wait()
        self.play(TransformFromCopy(answers_2, answers_3))
        self.wait(3)

        # Step 8: Check for valid log values
        final = MathTex(r"\log y\text{ is undefined for } y \leq 0", color=YELLOW).to_edge(DOWN)
        self.play(Write(final))
        self.wait()
        self.play(FadeOut(answers_1, answers_2, shift=UP), final.animate.to_edge(UP).set_color(WHITE).scale(1.75),
                 answers_3.animate.shift(2*UP))
        self.wait(3)

        # Final boxed answer
        solution = MathTex(r"\boxed{y = 4}", color=YELLOW).scale(4)
        solution_text = Tex("Therefore:").to_edge(UP).scale(1.5)
        final_group = VGroup(final, answers_3)
        self.play(Transform(final, solution_text), Transform(answers_3, solution))
        self.wait()
        self.play(Indicate(answers_3))
        self.wait(3)
        self.play(ShrinkToCenter(final_group))
        self.wait()

        # Outro
        final_text = Tex("Thank you for watching!", color=YELLOW).scale(1.5)
        self.play(Write(final_text))
        self.wait()
        self.play(logo_corner.animate.move_to(ORIGIN).scale(3), 
                  final_text.animate.to_edge(DOWN).set_color(WHITE))
        self.wait(2)
        self.play(FadeOut(final_text, logo_corner))
        self.wait()