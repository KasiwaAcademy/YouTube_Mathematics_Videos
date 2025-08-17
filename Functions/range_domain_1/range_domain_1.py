from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30
config.disable_caching = True

class DomainRange(VoiceoverScene):
    def construct(self):
        # Set Up speech services
        self.set_speech_service(GTTSService(lang="en", transcription_model="base"))

        # Add background image
        background = ImageMobject("./Image/chalk_board.jpg")
        background.set_z_index(-1)
        background.scale_to_fit_height(config.frame_height)
        background.scale_to_fit_width(config.frame_width)
        self.add(background)

        # Load and position logo image
        logo = ImageMobject("./Image/logo.png")
        logo_corner = logo.scale(0.15)
        logo_corner.to_corner(DR)
        self.add(logo_corner)

        # Intro
        text = """
                Hello and Welcome! In today's lesson we'll explore how to calculate the domain of a function when the range \
                is given. Stay with us here at <bookmark mark="A"/> Kasiwa Academy as we continue growing our Mathematical skills together. 
                 """
        with self.voiceover(text=text) as tracker:
            title = Tex(r"\textbf{Finding Domain given Range.}", color=YELLOW)
            institution = Tex(r"@Kasiwa Academy")
            self.play(Write(title))
            self.wait()
            self.play(title.animate.shift(UP).scale(1.5).set_color(WHITE))
            self.wait_until_bookmark("A")
            self.play(FadeIn(institution, shift=UP))
        self.wait(2)

        # Slide 1
        text_1 = """
                Let us begin by introducing our problem. We are given a function, <bookmark mark="A"/> g of x which is equal to two-thirds of the \
                squareroot of x plus one. We are asked to calculate the <bookmark mark="B"/> domain when the <bookmark mark="C"/> range is equal to <bookmark mark="D"/> six.
                 """
        with self.voiceover(text=text_1) as tracker:
            sub_title_1 = Tex(r"\textbf{Problem Statement}:", color=YELLOW).to_edge(DOWN)
            statement_1 = Tex(r"Given that ", r"$g(x) = \frac{2\sqrt{x}}{3} + 1$ ", r"calculate the \\",
                              r"\textbf{domain} ", r"when the ", r"\textbf{range} ", "is ", r"$6$.").scale(1.5)
            self.play(Write(sub_title_1))
            self.wait()
            self.play(FadeOut(title, institution, shift=UP), sub_title_1.animate.to_edge(UP).set_color(YELLOW_B).scale(1.5),
                     FadeIn(statement_1))
            self.wait_until_bookmark("A")
            self.play(Indicate(statement_1[1]), run_time=tracker.time_until_bookmark("B", limit=1))
            self.wait_until_bookmark("B")
            self.play(Indicate(statement_1[3]), run_time=tracker.time_until_bookmark("C", limit=1))
            self.wait_until_bookmark("C")
            self.play(Indicate(statement_1[5]), run_time=tracker.time_until_bookmark("D", limit=1))
            self.wait_until_bookmark("D")
            self.play(Indicate(statement_1[7]))
        self.wait()

        # Slide 2
        text_2 = """
                Before we start solving our problem, let us recall some important definitions. <bookmark mark="A"/> A function  is a rule or \
                relationship that assigns each input exactly one output. <bookmark mark="B"/> The input usually writtenas x is called the independent \
                variable. <bookmark mark="C"/> The output written as f of x or as in our case g of x is the independent variable. <bookmark mark="D"/> The domain represents \
                all possible input values of the independent variable x. <bookmark mark="E"/> The range represents all possible output values of the dependent \
                variable y, which is represented as g of x in our problem. In other words, the domain tells us what values x can take \
                and the range tells us what-values-the-function-produces-as-output.
                 """
        with self.voiceover(text=text_2) as tracker:
            sub_title_2 = Tex(r"\textbf{Define terms}:", color=YELLOW).to_edge(DOWN)
            statement_2 = Tex(r"\textbf{Function}:\\",
                              r"A rule or relationship that assigns each input \\",
                              r"exactly one output.").move_to([0, 1.75, 0]).set_color_by_tex("Function", YELLOW_D)
            statement_3 = VGroup(
                Tex(r"\textbf{Input}:", " $x$", " (independent variable).").set_color_by_tex("Input", YELLOW_D),
                Tex(r"\textbf{Output}:", " $f(x)$", " (dependent variable).").set_color_by_tex("Output", YELLOW_D),
                Tex(r"\textbf{Domain}:", " all allowed inputs.").set_color_by_tex("Domain", YELLOW_D),
                Tex(r"\textbf{Range}:", " all possible outputs.").set_color_by_tex("Range", YELLOW_D)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to([0, -1, 0])
            self.play(Write(sub_title_2))
            self.wait()
            self.play(FadeOut(sub_title_1, statement_1, shift=UP), sub_title_2.animate.to_edge(UP).set_color(YELLOW_B).scale(1.5))
            self.wait_until_bookmark("A")
            self.play(Write(statement_2), run_time=tracker.time_until_bookmark("B", limit=1))
            self.wait_until_bookmark("B")
            self.play(Write(statement_3[0]), run_time=tracker.time_until_bookmark("C", limit=1))
            self.wait_until_bookmark("C")
            self.play(Write(statement_3[1]), run_time=tracker.time_until_bookmark("D", limit=1))
            self.wait_until_bookmark("D")
            self.play(Write(statement_3[2]), run_time=tracker.time_until_bookmark("E", limit=1))
            self.wait_until_bookmark("E")
            self.play(Write(statement_3[3]))
        self.wait()

        # Slide 3
        text_3 = """
                Now that we have defined important terms, lets start with our given <bookmark mark="A"/> function. It is important to note that \
                the output part of our function, <bookmark mark="B"/> g of x, can also be represented by the small letter y, which means that our function \
                can still be written-as <bookmark mark="C"/> -y-is-equal-to-two-thirds-of-square-root-of-x+1.
                 """
        with self.voiceover(text=text_3) as tracker:
            sub_title_3 = Tex(r"\textbf{Start with the given function}:", color=YELLOW).to_edge(DOWN)
            eq_group_1 = VGroup(
                MathTex(r"g(x) = \frac{2\sqrt{x}}{3} + 1"),
                MathTex(r"y = g(x)"),
                MathTex(r"y = \frac{2\sqrt{x}}{3} + 1")
            ).arrange(DOWN, buff=0.5).scale(1.3)
            self.play(Write(sub_title_3))
            self.wait_until_bookmark("A")
            self.play(FadeOut(sub_title_2, statement_2, statement_3, shift=UP), Write(eq_group_1[0]),
                     sub_title_3.animate.to_edge(UP).set_color(YELLOW_B).scale(1.5), run_time=tracker.time_until_bookmark("B", limit=1))
            self.wait_until_bookmark("B")
            self.play(TransformFromCopy(eq_group_1[0], eq_group_1[1]), run_time=tracker.time_until_bookmark("C", limit=1))
            self.wait_until_bookmark("C")
            self.play(TransformFromCopy(eq_group_1[1], eq_group_1[2]))
        self.wait()

        # Slide 4
        text_4 = """
                Since the range is given as six, we set y equal to six. This is the value for the output part of our function.
                 """
        with self.voiceover(text = text_4) as tracker:
            sub_title_4 = Tex(r"\textbf{Express output $y$ as Range}:", color=YELLOW).to_edge(DOWN)
            eq_group_2 = VGroup(
                MathTex(r"Range = 6 \qquad \Longrightarrow \qquad y = 6"),
                MathTex(r"6 = \frac{2\sqrt{x}}{3} + 1")
            ).arrange(DOWN, buff=0.5).scale(1.3).move_to([0, -1, 0])
            self.play(Write(sub_title_4))
            self.wait()
            self.play(FadeOut(sub_title_3, eq_group_1[0], eq_group_1[1], shift=UP),
                      eq_group_1[2].animate.move_to([0, 2, 0]), 
                      sub_title_4.animate.to_edge(UP).set_color(YELLOW_B).scale(1.5))
            self.wait()
            self.play(Write(eq_group_2[0]))
            self.wait()
            self.play(Write(eq_group_2[1]))
        self.wait(2)

        # Slide 5
        text_5 = """
                Now that we have successfully substituted six for y in our function, let us solve for the square-root of x. \
                We will firsty remove the constant term one from the right-hand-side of the equation. We will achieve this by \
                <bookmark mark="A"/> subtracting 1 from both sides, this will give us a <bookmark mark="B"/> 5 in the left-hand-side and two-third-square-root-of-x in the \
                right-hand-side.
                 """
        with self.voiceover(text=text_5) as tracker:
            sub_title_5 = Tex(r"\textbf{Solve for $\sqrt{x}$} :", color=YELLOW).to_edge(DOWN)
            statement_4 = Tex(r"Subtract $1$ from both sides.").move_to([0, 2.5, 0])
            eq_group_3 = VGroup(
                MathTex(r"6 - 1 = \frac{2\sqrt{x}}{3} + 1 - 1"),
                MathTex(r"5 = \frac{2\sqrt{x}}{3}")
            ).arrange(DOWN, buff=0.5).scale(1.1).move_to([0, -1.5, 0])
            self.play(Write(sub_title_5))
            self.wait()
            self.play(FadeOut(sub_title_4, eq_group_1[2], eq_group_2[0], shift=UP),
                     eq_group_2[1].animate.move_to([0, 1, 0]), sub_title_5.animate.to_edge(UP).set_color(YELLOW_B).scale(1.5),
                     GrowFromCenter(statement_4))
            self.wait_until_bookmark("A")
            self.play(TransformFromCopy(eq_group_2[1], eq_group_3[0]), run_time=tracker.time_until_bookmark("B", limit=1))
            self.wait_until_bookmark("B")
            self.play(TransformFromCopy(eq_group_3[0], eq_group_3[1]))
        self.wait()

        # Slide 6
        text_6 = """
                Secondly we will have to remove 3 from the right-hand-side by multiplying by <bookmark mark="A"/> 3 in-both-sides-of-the-equation. \
                The threes from the right-hand-side will cancel each other leaving us with <bookmark mark="B"/> 2-square-root-of-x-in-the-right-hand-side \
                and-15-in-the-left-hand-side.
                 """
        with self.voiceover(text=text_6) as tracker:
            statement_5 = Tex(r"Multiply both sides by $3$.", color=YELLOW).to_edge(DOWN)
            eq_group_4 = VGroup(
                MathTex(r"3 \times 5 = \frac{2\sqrt{x}}{3} \times 3"),
                MathTex(r"15 = 2\sqrt{x}")
            ).arrange(DOWN, buff=0.5).scale(1.1).move_to([0, -1, 0])
            self.play(Write(statement_5))
            self.wait()
            self.play(FadeOut(eq_group_2[1], eq_group_3[0], statement_4, shift=RIGHT), eq_group_3[1].animate.move_to([0, 1.3, 0]),
                     statement_5.animate.move_to([0, 2.4, 0]).set_color(WHITE))
            self.wait_until_bookmark("A")
            self.play(TransformFromCopy(eq_group_3[1], eq_group_4[0]), run_time=tracker.time_until_bookmark("B", limit=1))
            self.wait_until_bookmark("B")
            self.play(TransformFromCopy(eq_group_4[0], eq_group_4[1]))
        self.wait()

        # Slide 7
        text_7 = """
                As the last step in solving for the square-root of x, we will remove 2 from the right-hand-side by dividing by <bookmark mark="A"/> 2 in both\
                sides. This will leave us with the <bookmark mark="B"/> square-root-of-x-in-one side and fifteen over 2 in the other side.
                 """
        with self.voiceover(text=text_7) as tracker:
            statement_6 = Tex(r"Divide both sides by $2$.", color=YELLOW).to_edge(DOWN)
            eq_group_5 = VGroup(
                MathTex(r"\frac{2\sqrt{x}}{2} = \frac{15}{2}"),
                MathTex(r"\sqrt{x} = \frac{15}{2}")
            ).arrange(DOWN, buff=0.5).scale(1.1).move_to([0, -1, 0])
            self.play(Write(statement_6))
            self.wait()
            self.play(FadeOut(statement_5, eq_group_3[1], eq_group_4[0], shift=UP),
                      eq_group_4[1].animate.move_to([0, 1.3, 0]), 
                      statement_6.animate.move_to([0, 2.4, 0]).set_color(WHITE))
            self.wait_until_bookmark("A")
            self.play(TransformFromCopy(eq_group_4[1], eq_group_5[0]), run_time=tracker.time_until_bookmark("B", limit=1))
            self.wait_until_bookmark("B")
            self.play(TransformFromCopy(eq_group_5[0], eq_group_5[1]))
        self.wait()

        # Slide 8
        text_8 = """
                In finding the domain when the range is given, we are simply trying to determine the input value x \
                from the output value y. To do this, we <bookmark mark="A"/> square both sides of the equation. This leaves us with <bookmark mark="B"/> x on the \
                left-hand-side and 225 over 4 on the right-hand-side. Simplifying 225 over 4 gives us <bookmark mark="C"/> 56.25.
                 """
        with self.voiceover(text=text_8) as tracker:
            sub_title_6 = Tex(r"\textbf{Solve for $x$} :", color=YELLOW).to_edge(DOWN)
            statement_7 = Tex(r"Square both sides to solve for $x$.").move_to([0, 2.4, 0])
            eq_group_6 = VGroup(
                MathTex(r"\sqrt{x}^2 = \left(\frac{15}{2}\right)^2"),
                MathTex(r"x = \frac{225}{4}"),
                MathTex(r"x = 56.25")
            ).arrange(DOWN, buff=0.5).scale(1).move_to([0, -1.3, 0])
            self.play(Write(sub_title_6))
            self.wait()
            self.play(FadeOut(sub_title_5, statement_6, eq_group_4[1], eq_group_5[0], shift=UP),
                     sub_title_6.animate.to_edge(UP).set_color(YELLOW_B).scale(1.5),
                     eq_group_5[1].animate.move_to([0, 1.3, 0]), GrowFromCenter(statement_7))
            self.wait_until_bookmark("A")
            self.play(TransformFromCopy(eq_group_5[1], eq_group_6[0]), run_time=tracker.time_until_bookmark("B", limit=1))
            self.wait_until_bookmark("B")
            self.play(TransformFromCopy(eq_group_6[0], eq_group_6[1]), run_time=tracker.time_until_bookmark("C", limit=1))
            self.wait_until_bookmark("C")
            self.play(TransformFromCopy(eq_group_6[1], eq_group_6[2]))
            self.play(FadeOut(eq_group_5[1]), eq_group_6.animate.move_to([ORIGIN]))
        self.wait()

        # Slide 9
        text_9 = """
                Therefore, the domain corresponding to the range value of six is x = 56.25.
                 """
        with self.voiceover(text=text_9) as tracker:
            sub_title_7 = Tex(r"\textbf{Final Answer}:", color=YELLOW).to_edge(DOWN)
            final_answer = Tex(r"\boxed{\textbf{56.25}}", color=YELLOW_C).shift(DOWN*1.5).scale(2)
            self.play(Write(sub_title_7))
            self.wait()
            self.play(FadeOut(sub_title_6, eq_group_6[0], eq_group_6[1], statement_7, shift=UP),
                     sub_title_7.animate.to_edge(UP).set_color(YELLOW_B).scale(1.5),
                     eq_group_6[2].animate.move_to([0, 1.5, 0]).scale(1.5))
            self.wait()
            self.play(FadeIn(final_answer))
            self.wait()
            self.play(Indicate(final_answer))
            self.wait(1)
            final_group = VGroup(final_answer, eq_group_6[2], sub_title_7)
            self.play(ShrinkToCenter(final_group))
        
        #Outro
        outro_text = """
                    Thank you for watching. See you in our next video.
                     """
        with self.voiceover(text=outro_text) as tracker:
            final_text = Tex("Thank you for watching!", color=YELLOW_B).scale(1.5)
            self.play(Write(final_text))
            self.wait()
            self.play(logo_corner.animate.move_to(ORIGIN).scale(3), 
                        final_text.animate.to_edge(DOWN).set_color(WHITE))
            self.wait(2)
            self.play(FadeOut(final_text, logo_corner))