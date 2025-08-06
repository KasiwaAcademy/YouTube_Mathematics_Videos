from manim import *

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30

class ChangeSubjectFormula(Scene):
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
        title = Tex(r"Changing the Subject of Formula", color=YELLOW)
        institution = Tex(r"@Kaswia Academy")
        self.play(Write(title))
        self.wait()
        self.play(title.animate.shift(UP).scale(1.5).set_color(WHITE), FadeIn(institution, shift=UP))
        self.wait(2)

        # Problem Statement
        statement = Tex(r"Problem Statement:", color=YELLOW)
        question_1 = Tex(r"Make $k$ the subject of the Formula")
        question_2 = MathTex(r"x = \frac{b - k^3}{k^3}").shift(1.5*DOWN)
        self.play(FadeOut(title, institution, shift=RIGHT), Write(statement))
        self.wait()
        self.play(statement.animate.to_edge(UP).scale(1.5).set_color(WHITE))
        self.wait()
        self.play(FadeIn(question_1, question_2, shift=UP))
        self.wait()
        self.play(question_1.animate.shift(UP).scale(1.3), question_2.animate.shift(UP).scale(1.5))
        self.wait()
        self.play(Indicate(question_2))
        self.wait(3)
        
        # Step 1
        text_1 = Tex(r"Start with the given equation:", color=YELLOW).shift(2*DOWN)
        eq1 = MathTex(r"x = \frac{b - k^3}{k^3}").scale(1.5)
        self.play(Write(text_1))
        self.wait()
        self.play(FadeOut(statement, question_1, question_2, shift=UP), 
                  text_1.animate.to_edge(UP).scale(1.75).set_color(WHITE), FadeIn(eq1, shift=UP))
        self.wait(3)

        # Step 2 - slide_1 
        text_2 = Tex(r"Multiply both sides by $k^3$:", color=YELLOW).shift(2*DOWN)
        eq2 = MathTex(r"k^3 \times x = \frac{b - k^3}{k^3} \times k^3").shift(DOWN).scale(1.5)
        self.play(Write(text_2))
        self.wait()
        self.play(FadeOut(text_1, shift=UP), text_2.animate.to_edge(UP).scale(1.5).set_color(WHITE),
                 eq1.animate.shift(2*UP))
        self.wait()
        self.play(TransformFromCopy(eq1, eq2))
        self.wait(3)

        # Step 2 - slide_2
        eq3 = MathTex(r"k^3 \times x = b - k^3").scale(1.5)
        eq4 = MathTex(r"k^3x = b - k^3").shift(2*DOWN).scale(1.5)
        self.play(FadeOut(eq1, shift=UP), eq2.animate.shift(3*UP))
        self.wait()
        self.play(TransformFromCopy(eq2, eq3))
        self.wait()
        self.play(TransformFromCopy(eq3, eq4))
        self.wait(3)

        # Step 3
        text_3 = Tex(r"Add $k^3$ to both sides of the equation:", color=YELLOW).to_edge(DOWN)
        eq5 = MathTex(r"k^3x + k^3 = b - k^3 + k^3").scale(1.5)
        eq6 = MathTex(r"k^3x + k^3 = b").shift(2*DOWN).scale(1.5)
        self.play(Write(text_3))
        self.wait()
        self.play(FadeOut(text_2, eq1, eq2, eq3, shift=UP), text_3.animate.to_edge(UP).scale(1.5).set_color(WHITE),
                 eq4.animate.shift(4*UP))
        self.wait()
        self.play(TransformFromCopy(eq4, eq5))
        self.wait()
        self.play(TransformFromCopy(eq5, eq6))
        self.wait(3)

        # Step 4
        text_4 = Tex(r"Factorise the left-hand side of the equation:", color=YELLOW).to_edge(DOWN)
        eq7 = MathTex(r"k^3(x + 1) = b").shift(DOWN).scale(1.5)
        self.play(Write(text_4))
        self.wait()
        self.play(FadeOut(text_3, eq4, eq5, shift=UP), text_4.animate.to_edge(UP).scale(1.3).set_color(WHITE),
                 eq6.animate.shift(3*UP))
        self.play(TransformFromCopy(eq6, eq7))
        self.wait(3)

        # Step 4
        text_5 = Tex(r"Devide both sides by $x + 1$ :", color=YELLOW).to_edge(DOWN)
        eq8 = MathTex(r"\frac{k^3(x + 1)}{(x + 1)} = \frac{b}{(x + 1)}").scale(1.5)
        eq9 = MathTex(r"k^3 = \frac{b}{x + 1}").shift(2*DOWN).scale(1.5)
        self.play(Write(text_5))
        self.wait()
        self.play(FadeOut(text_4, eq6, shift = UP), text_5.animate.to_edge(UP).scale(1.5).set_color(WHITE),
                 eq7.animate.shift(3*UP))
        self.wait()
        self.play(TransformFromCopy(eq7, eq8))
        self.wait()
        self.play(TransformFromCopy(eq8, eq9))
        self.wait(3)
        
        # Step 5 - slide_1
        text_6 = Tex(r"Take the cube-root of both sides:", color=YELLOW).to_edge(DOWN)
        eq1 = MathTex(r"k^3 = \frac{b}{x + 1}").shift(2*UP).scale(1.5)
        eq10 = MathTex(r"\sqrt[3]{k^3} = \sqrt[3]{\frac{b}{x + 1}}").shift(2*DOWN).scale(1.5)
        self.play(Write(text_6))
        self.wait()
        self.play(FadeOut(text_5, eq7, eq8, shift=UP), text_6.animate.to_edge(UP).scale(1.5).set_color(WHITE),
                 eq9.animate.shift(3*UP))
        self.wait()
        self.play(TransformFromCopy(eq9, eq10))
        self.wait(3)

        # Step 5 -slide_2
        eq11 = MathTex(r"k = \sqrt[3]{\frac{b}{x + 1}}").shift(2*DOWN).scale(1.5)
        self.play(FadeOut(eq9, shift=UP), eq10.animate.shift(3*UP))
        self.wait()
        self.play(TransformFromCopy(eq10, eq11))
        self.wait(3)
        
        # Final Answer
        text_7 = Tex(r"The Final Answer is:").to_edge(UP).scale(1.5)
        final_answer = MathTex(r"\boxed{k = \sqrt[3]{\frac{b}{x + 1}}}", color=YELLOW).scale(3)
        final_answer_group = VGroup(text_7, eq11, final_answer)                                                                                
        self.play(FadeOut(text_6, eq10, shift=UP), eq11.animate.shift(2*UP).scale(2))
        self.wait()
        self.play(Write(text_7), Transform(eq11, final_answer))
        self.wait()
        self.play(Indicate(final_answer))
        self.wait(3)
        self.play(ShrinkToCenter(final_answer_group))
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
