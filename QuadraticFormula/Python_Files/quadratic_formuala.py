from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_rate = 30

class Quadratic(Scene):
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
        
        # Title
        title = Tex("Deriving the Quadratic Formula").shift(UP).scale(1.75)
        institution = Tex(r"@Kasiwa Academy")
        self.play(Write(title), FadeIn(institution))
        self.wait()
        self.play(FadeOut(title, institution))
        self.wait()

        # Step 1
        explanation = Tex("Start with the general quadratic equation:").scale(1.5).to_edge(UP)
        eq1 = MathTex("ax^2 + bx + c = 0").scale(1.75)
        self.add(explanation)
        self.wait()
        self.play(Write(eq1))
        self.wait()
        self.play(FadeOut(explanation, eq1))
        self.wait()

        # Step 2
        explanation = Tex("Divide the entire equation by $a$ to simplify:").scale(1.5).to_edge(UP)
        eq1 = MathTex(r"ax^2 + bx + c").shift(2*UP).scale(1.5)
        eq2 = MathTex(r"\frac{ax^2}{a} + \frac{bx}{a} + \frac{c}{a} = \frac{0}{a}").scale(1.5)
        eq3 = MathTex(r"x^2 + \frac{b}{a}x + \frac{c}{a} = 0").next_to(eq2, direction = DOWN, buff = 0.5).scale(1.5)
        self.add(explanation)
        self.wait()
        self.play(Write(eq1))
        self.wait()
        self.play(TransformFromCopy(eq1, eq2))
        self.wait()
        self.play(TransformFromCopy(eq2, eq3))
        self.wait(2)
        self.play(FadeOut(explanation, eq1, eq2, eq3))
        self.wait()

        # Step 3
        explanation = Tex("Move the constant term to the right side:").to_edge(UP).scale(1.5)
        eq1 = MathTex(r"x^2 + \frac{b}{a}x + \frac{c}{a} = 0").shift(1.5*UP).scale(1.5)
        eq2 = MathTex(r"x^2 + \frac{b}{a}x = -\frac{c}{a}").shift(1.5*DOWN).scale(1.5)
        self.add(explanation)
        self.wait()
        self.play(Write(eq1))
        self.wait()
        self.play(TransformFromCopy(eq1, eq2))
        self.wait(2)
        self.play(FadeOut(explanation, eq1, eq2))
        self.wait()

        # Step 4
        explanation = Tex("Complete the square on the left side:").scale(1.5).to_edge(UP)
        eq1 = MathTex(r"x^2 + \frac{b}{a}x = -\frac{c}{a}").shift(1.5*UP).scale(1.5)
        eq2 = MathTex(r"x^2 + \frac{b}{a}x + \left(\frac{b}{2a}\right)^2 = -\frac{c}{a} + \left(\frac{b}{2a}\right)^2").shift(DOWN).scale(1.5)
        self.add(explanation)
        self.wait()
        self.play(Write(eq1))
        self.wait()
        self.play(TransformFromCopy(eq1, eq2))
        self.wait(2)
        self.play(FadeOut(explanation, eq1, eq2))
        self.wait()

        # Step 5
        explanation = Tex("Factor the perfect square on the left:").scale(1.5).to_edge(UP)
        eq1 = MathTex(r"x^2 + \frac{b}{a}x + \left(\frac{b}{2a}\right)^2 = -\frac{c}{a} + \left(\frac{b}{2a}\right)^2").shift(1.5*UP).scale(1.5)
        eq2 = MathTex(r"\left(x + \frac{b}{2a}\right)^2 = -\frac{c}{a} + \frac{b^2}{4a^2}").shift(DOWN).scale(1.5)
        self.add(explanation)
        self.wait()
        self.play(Write(eq1))
        self.wait()
        self.play(TransformFromCopy(eq1, eq2))
        self.wait(2)
        self.play(FadeOut(explanation, eq1,eq2))
        self.wait()

        # Step 6
        explanation = Tex("Simplify the right-hand side:").scale(1.5).to_edge(UP)
        eq1 = MathTex(r"\left(x + \frac{b}{2a}\right)^2 = -\frac{c}{a} + \frac{b^2}{4a^2}").shift(2*UP).scale(1.5)
        eq2 = MathTex(r"\left(x + \frac{b}{2a}\right)^2 = \frac{b^2 - 4ac}{4a^2}").shift(DOWN).scale(1.5)
        self.add(explanation)
        self.wait()
        self.play(Write(eq1))
        self.wait()
        self.play(TransformFromCopy(eq1, eq2))
        self.wait(2)
        self.play(FadeOut(explanation, eq1, eq2))
        self.wait()

        # Step 7
        explanation = Tex("Take square root on both sides:").scale(1.5).to_edge(UP)
        eq1 = MathTex(r"\sqrt{\left(x + \frac{b}{2a}\right)^2} = \sqrt{\frac{b^2 - 4ac}{4a^2}}").shift(1.5*UP).scale(1.5)
        eq2 = MathTex(r"x + \frac{b}{2a} = \pm \frac{\sqrt{b^2 - 4ac}}{2a}").shift(2*DOWN).scale(1.5)
        self.add(explanation)
        self.wait()
        self.play(Write(eq1))
        self.wait()
        self.play(TransformFromCopy(eq1, eq2))
        self.wait(2)
        self.play(FadeOut(explanation, eq1, eq2))
        self.wait()

        # Step 8
        explanation = Tex("Solve for $x$:").to_edge(UP).scale(1.5)
        eq1 = MathTex(r"x + \frac{b}{2a} = \pm \frac{\sqrt{b^2 - 4ac}}{2a}").shift(2*UP).scale(1.5)
        eq2 = MathTex(r"x = - \frac{b}{2a} \pm \frac{\sqrt{b^2 - 4ac}}{2a}").scale(1.5)
        eq3 = MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}").next_to(eq2, direction = DOWN, buff = 1).scale(1.5)
        self.add(explanation)
        self.wait()
        self.play(Write(eq1))
        self.wait()
        self.play(TransformFromCopy(eq1, eq2))
        self.wait()
        self.play(TransformFromCopy(eq2, eq3))
        self.wait(2)
        self.play(FadeOut(explanation, eq1, eq2, eq3))
        self.wait()

        # Step 9 (Final Answer)
        explanation = Tex(r"This is the Quadratic Equation:").shift(2*UP).scale(1.5)
        eq1 = MathTex(r"\boxed{x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}}").shift(DOWN).scale(1.75)
        self.add(explanation)
        self.wait()
        self.play(FadeIn(eq1))
        self.wait(2)
        self.play(FadeOut(explanation, eq1))
        self.wait()

        # Outro
        final_text = Tex("Thank you for watching!").to_edge(DOWN).scale(1.75)
        logo_final = logo.move_to(ORIGIN).scale(3)
        self.play(Write(final_text))
        self.wait()
        self.play(Transform(logo_corner, logo_final))
        self.wait(2)
        self.play(FadeOut(final_text, logo_final))