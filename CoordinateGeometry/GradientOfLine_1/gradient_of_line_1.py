from manim import *

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30
config.disable_caching = True

class GradientOfLine(Scene):
    def construct(self):

        # Create a custom Latex template that includes the cancel package
        my_template = TexTemplate()
        my_template.add_to_preamble(r"\usepackage{cancel}")

        # Load and position logo image
        logo = ImageMobject("./logo.png")
        logo_corner = logo.scale(0.15)
        logo_corner.to_corner(DR, buff=-0.2)
        self.add(logo_corner)

        # Intro
        title = Tex(r"Solving a Coordinate Geometry Problem.", color=YELLOW)
        institution = Tex(r"@Kasiwa Academy")
        self.play(Write(title))
        self.wait()
        self.play(title.animate.shift(UP).scale(1.3).set_color(YELLOW_B), FadeIn(institution, shift=UP))
        self.wait(2)

        # Problem Statement
        sub_title_1 = Tex(r"Problem Statement:", color=YELLOW).to_edge(DOWN)
        statement_1 = Tex(r"The gradient of a line joining two points \textbf{B} $= (4, 2b)$ and \\"
                          r"\textbf{C} $= (6, -8)$ is $7$. Find the value of $b$.")
        self.play(Write(sub_title_1))
        self.wait()
        self.play(FadeOut(title, institution, shift=UP), sub_title_1.animate.to_edge(UP).scale(1.3).set_color(WHITE), 
                  FadeIn(statement_1, shift=UP))
        self.wait()
        self.play(statement_1.animate.scale(1.1))
        self.wait(2)

        # Solution
        sub_title_2 = Tex(r"Solution:", color=YELLOW).to_edge(DOWN)
        first_group = VGroup(
            Tex(r"$B = (4, 2b)$ and $C = (6, -8)$"),
            Tex(r"gradient = $m$ = $7$"),
            MathTex(r"\Rightarrow m = \frac{y2 - y1}{x2 - x1}"),
            MathTex(r"\Rightarrow 7 = \frac{-8 - 2b}{6 - 4}"),
            MathTex(r"\Rightarrow 7 = \frac{-8 -2b}{2}"),
            MathTex(r"\Rightarrow 2 \times 7 = \frac{-8 - 2b}{2} \times 2")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.75).to_edge(LEFT).scale(0.75).shift(DOWN*0.5)
        self.play(Write(sub_title_2))
        self.wait()
        self.play(FadeOut(sub_title_1, statement_1, shift=UP), Write(first_group[0]),
                 sub_title_2.animate.to_edge(UP).set_color(YELLOW_B).scale(1.3))
        self.wait(2)
        self.play(Write(first_group[1]))
        self.wait(2)
        self.play(Write(first_group[2]))
        self.wait(2)
        self.play(TransformFromCopy(first_group[2], first_group[3]))
        self.wait(2)
        self.play(TransformFromCopy(first_group[3], first_group[4]))
        self.wait(2)
        self.play(TransformFromCopy(first_group[4], first_group[5]))
        self.wait(2)
        second_group = VGroup(
            MathTex(r"\Rightarrow 14 = \frac{-8 - 2b}{\cancel{2}} \times \cancel{2}",
                   tex_template=my_template),
            MathTex(r"\Rightarrow 14 = -8 - 2b"),
            MathTex(r"\Rightarrow 14 + 8 = -8 + 8 - 2b"),
            MathTex(r"\Rightarrow 22 = -2b"),
            MathTex(r"\Rightarrow \frac{22}{-2} = \frac{-2b}{-2}"),
            MathTex(r"\Rightarrow \frac{22}{-2} = \frac{\cancel{-2}b}{\cancel{-2}}", 
                    tex_template=my_template),
            MathTex(r"\Rightarrow b = -11")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.75).to_edge(RIGHT).scale(0.75).shift(DOWN*0.5)
        self.play(TransformFromCopy(first_group[5], second_group[0]))
        self.wait(2)
        self.play(TransformFromCopy(second_group[0], second_group[1]))
        self.wait(2)
        self.play(TransformFromCopy(second_group[1], second_group[2]))
        self.wait(2)
        self.play(TransformFromCopy(second_group[2], second_group[3]))
        self.wait(2)
        self.play(TransformFromCopy(second_group[3], second_group[4]))
        self.wait(2)
        self.play(TransformFromCopy(second_group[4], second_group[5]))
        self.wait(2)
        self.play(TransformFromCopy(second_group[5], second_group[6]))
        self.wait(2)

        # Final Answer
        sub_title_3 = Tex(r"Final Answer:", color=YELLOW_B).to_edge(UP).scale(1.3)
        final_answer = MathTex(r"\boxed{x = -11}", color=YELLOW_C).scale(2)
        final_group = VGroup(first_group, second_group)
        self.play(ReplacementTransform(sub_title_2, sub_title_3), ShrinkToCenter(final_group),
                 FadeIn(final_answer, shift=UP))
        self.wait()
        self.play(Indicate(final_answer))
        self.wait(2)
        
        #Outro
        final_text = Tex("Thank you for watching!", color=YELLOW_B)
        self.play(Write(final_text), FadeOut(final_answer, sub_title_3, shift=RIGHT))
        self.wait()
        self.play(logo_corner.animate.move_to(ORIGIN).scale(3), 
                    final_text.animate.to_edge(DOWN).set_color(WHITE).scale(1.3))
        self.wait()
        self.play(FadeOut(final_text, logo_corner))
        self.wait()