# Circle_Geometry_One

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30

class CircleGeometry(Scene):
    def construct(self):
        # Configurations
        main_color = BLUE_A
        accent_color = YELLOW
        secondary_color = GREEN
        text_color = WHITE
        
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
        title = Tex(r"Solving Circle Geometry Problem", color=YELLOW)
        institution = Tex(r"@Kaswia Academy")
        self.play(Write(title))
        self.wait()
        self.play(title.animate.shift(UP).scale(1.5).set_color(WHITE), FadeIn(institution, shift=UP))
        self.wait(2)

        # Problem Statement
        text_1 = Tex(r"Problem Statement:", color=YELLOW)
        text_2 = Tex(r"Given a circle $ABCD$ with centre $O$, in which\\"
                     r"$BC$ = $BD$ and $\angle DAB$ = $52^\circ$").shift(2*UP)
        text_3 = Tex(r"Calculate the value of angle $ABC$.").to_edge(DOWN)
        
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

        ## Angles and Ancillaries
        angle_ABC = Angle(Line(B,C), Line(B,A), radius=0.65, color=accent_color, other_angle=True, stroke_width=2)
        angle_ABC_label = Tex(r"116$^\circ$", color=text_color).scale(0.7).next_to(B, DOWN, buff=0.7).shift(RIGHT*0.2)
        angle_BAC = Angle(Line(A,C), Line(A,B), radius=0.8, color=secondary_color, stroke_width=2)
        angle_BAC_label = Tex(r"26$^\circ$", color=text_color).scale(0.5).next_to(A, UP+RIGHT, buff=0.6)
        angle_CAD = Angle(Line(A,D), Line(A,C), radius=0.8, color=secondary_color, stroke_width=2)
        angle_CAD_label = Tex(r"26$^\circ$", color=text_color).scale(0.5).next_to(A, UP+RIGHT, buff=0.82).shift(DOWN*0.45)
        angle_ABD = RightAngle(Line(B,A), Line(B,D), length=0.3, color=secondary_color, other_angle=True, stroke_width=2)
        arc_CD = ArcBetweenPoints(D, C, color=accent_color, stroke_width=2, radius=1.75)
        angle_CBD = Angle(Line(B,D), Line(B,C), radius=0.5, color=PURE_BLUE, stroke_width=2)
        angle_CBD_label = Tex(r"26$^\circ$", color=text_color).scale(0.4).next_to(B, DOWN+RIGHT, buff=0.5).shift(UP*0.3)
        angle_CAD_ref = Angle(Line(A,D), Line(A,C), radius=0.8, color=accent_color, stroke_width=2)
        a = Arc
        
        ## Highlight given info
        angle_DAB = Angle(Line(A,D), Line(A,B), radius=0.7, color=text_color, stroke_width=2)
        angle_DAB_label = Tex(r"52$^\circ$", color=text_color).scale(0.7).next_to(A, UP+RIGHT, buff=0.75).shift(DOWN*0.2)
        tick_BC = Line(BC.get_center() + 0.1*rotate_vector(BC.get_unit_vector(), PI/2), BC.get_center() - 0.1*rotate_vector(BC.get_unit_vector(), PI/2), color=text_color, stroke_width=2)
        tick_CD = Line(CD.get_center() + 0.1*rotate_vector(CD.get_unit_vector(), PI/2), CD.get_center() - 0.1*rotate_vector(CD.get_unit_vector(), PI/2), color=text_color,stroke_width=2)

        circle_group = VGroup(circle, AD, center_O, O_label, AC, AB, BC, CD, BD, labels,
                         angle_DAB, angle_DAB_label, tick_BC, tick_CD, angle_BAC, angle_CAD,
                             angle_ABD, arc_CD, angle_CBD, angle_CAD_ref, angle_BAC_label, angle_CAD_label, angle_CBD_label, angle_ABC, angle_ABC_label)
        AC.set_opacity(0)
        angle_BAC.set_opacity(0)
        angle_CAD.set_opacity(0)
        angle_ABD.set_opacity(0)
        arc_CD.set_opacity(0)
        angle_CBD.set_opacity(0)
        angle_CAD_ref.set_opacity(0)
        angle_BAC_label.set_opacity(0)
        angle_CAD_label.set_opacity(0)
        angle_CBD_label.set_opacity(0)
        angle_ABC.set_opacity(0).set_fill(DARKER_GRAY, opacity=0)
        angle_ABC_label.set_opacity(0)
        
        self.play(FadeOut(title, institution, scale=0.1), Write(text_1))
        self.wait()
        self.play(text_1.animate.to_edge(UP).scale(1.5).set_color(WHITE), 
                  FadeIn(text_2, text_3), SpinInFromNothing(circle_group))
        self.wait()
        self.wait(3)
        
        # Figure analysis
        ## Analysis one
        text_4 = Tex(r"Figure Analysis:", color=YELLOW).to_edge(DOWN)
        text_5 = Tex(r"We have a Cyclic Quadrilateral \\"
                     r"$ABCD$ with center at $O$").shift(DOWN*2)
        self.play(FadeTransform(text_3, text_4))
        self.wait()
        self.play(FadeOut(text_1, text_2, shift=UP),circle_group.animate.shift(1.5*UP), text_4.animate.to_edge(UP).set_color(WHITE).scale(1.3))
        self.wait()
        self.play(Write(text_5))
        self.play(Flash(center_O))
        self.wait()
        self.play(Indicate(AD), Indicate(AB), Indicate(BC), Indicate(CD))
        self.wait(3)

        ## Analysis two
        text_6 = Tex(r"The line segment $AD$ passes through the center $O$,\\"
                     r"which means $AD$ is a diameter of the circle.").shift(DOWN*2)
        self.play(FadeOut(text_5, shift=DOWN), Write(text_6))
        self.wait(0.5)
        self.play(Indicate(AD, scale_factor=1.5), Flash(center_O))
        self.wait(3)

        ## Analysis three
        text_7 = Tex(r"An angle subtended by a diameter at any point on the\\"
                     r"circumference is a right angle.\\"
                     r"Therefore, $\angle ABD$ = $90^\circ$").shift(DOWN*2.5)
        self.play(FadeOut(text_6, shift=DOWN), Write(text_7))
        self.wait(0.5)
        self.play(Indicate(AB), Indicate(BD), Flash(angle_ABD))
        self.wait(3)

        ## Analysis four
        text_8 = Tex(r"We are given that chord $BC$ = chord $CD$. Equal chords\\"
                     r"subtend equal angles at the circumference.").shift(DOWN*2)
        self.play(FadeOut(text_7, shift=DOWN), Write(text_8))
        self.wait(0.5)
        self.play(Indicate(BC), Indicate(CD))
        self.wait(3)

        ## Analysis five
        text_9 = Tex(r"We are given that angle $DAB$ = $52^\circ$.").shift(DOWN*2)
        self.play(FadeOut(text_8, shift=DOWN), Write(text_9))
        self.wait(0.5)
        self.play(Indicate(AB), Indicate(AD), Flash(angle_DAB))
        self.wait(3)

        ## Construct Line AC
        txt_1 = Tex(r"Construction:\\"
                    r"Construct line $AC$").shift(DOWN*2)
        self.play(FadeOut(text_9, shift=DOWN), Write(txt_1))
        self.wait()
        self.play(AC.animate.set_opacity(1))
        self.wait()
        self.play(AC.animate.set_color(main_color))
        self.wait(3)

        # Properties of Equal Chords
        ## Step 1
        text_10 = Tex(r"Use the Properties of Equal Chords:", color=accent_color).to_edge(DOWN)
        text_11 = Tex(r"Since chord $BC$ = chord $CD$, the angles they subtend\\"
                      r"from point A must be equal.").shift(DOWN*2)
        text_group_1 = VGroup(
            Tex(r"1. Chord $BC$ subtends $\angle BAC$").scale(0.85),
            Tex(r"2. Chord $CD$ subtends $\angle CAD$").scale(0.85),
            Tex(r"Therefore: $\angle BAC$ = $\angle CAD$").scale(0.85)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.75).move_to([2.2, -1, 0])
        self.play(Write(text_10))
        self.wait()
        self.play(FadeOut(text_4, shift=UP), FadeOut(txt_1, shift=RIGHT), 
                  text_10.animate.to_edge(UP).scale(1.2).set_color(WHITE), FadeIn(text_11))
        self.wait(2)
        self.play(circle_group.animate.to_edge(LEFT).shift(DOWN*1.5), text_11.animate.shift(UP*4).set_color(accent_color), Write(text_group_1[0]))
        self.play(BC.animate.set_color(PURE_RED), angle_BAC.animate.set_opacity(1).set_color(PURE_RED),
                 AB.animate.set_color(RED_D), AC.animate.set_color(GREEN_D))
        self.play(Flash(angle_BAC), Indicate(BC))
        #self.play(angle_BAC.animate.set_opacity(0))
        self.wait()
        self.play(Write(text_group_1[1]))
        self.play(CD.animate.set_color(PURE_BLUE), angle_CAD.animate.set_opacity(1).set_color(PURE_BLUE),
                 AD.animate.set_color(BLUE_D))
        self.play(Flash(angle_CAD), Indicate(CD))
        self.wait()
        self.play(Write(text_group_1[2]))
        self.play(Flash(angle_BAC), Flash(angle_CAD))
        self.wait(3)

        ## Step 2
        text_12 = Tex(r"$\angle DAB$ is the sum of $\angle BAC$ and $\angle CAD$").to_edge(DOWN)
        text_13 = Tex(r"$\angle DAB$ = $\angle BAC$ + $\angle CAD$ = $52^\circ$").shift(1.5*UP).scale(0.85)
        self.play(Write(text_12))
        self.wait()
        self.play(FadeOut(text_11, shift=UP), FadeOut(text_group_1, shift=LEFT), 
                  text_12.animate.shift(UP*5.75).set_color(accent_color), FadeIn(text_13),
                  circle_group.animate.move_to(ORIGIN).to_edge(DOWN))
        self.play(BC.animate.set_color(main_color), CD.animate.set_color(main_color), Indicate(angle_DAB), Indicate(angle_DAB_label))
        self.wait(0.5)
        self.play(Indicate(angle_BAC, color=PURE_RED), Indicate(angle_CAD, color=PURE_BLUE), Indicate(angle_DAB_label, color=PURE_BLUE))
        self.wait(3)

        ## Step 3
        text_14 = Tex(r"Since $\angle BAC = \angle CAD$, $AC$ is bisector of $\angle DAB$", color=accent_color).shift(UP*2.5)
        text_15 = Tex(r"$\angle CAD = \frac{\angle DAB}{2} = \frac{52^\circ}{2} = 26^\circ = \angle BAC$").shift(UP*1.5)
        self.play(FadeOut(text_12, text_13, shift=RIGHT), Write(text_14))
        self.wait()
        self.play(Write(text_15), angle_DAB.animate.set_opacity(0), angle_DAB_label.animate.set_opacity(0),
                 angle_BAC_label.animate.set_opacity(1), angle_CAD_label.animate.set_opacity(1))
        self.wait(3)

        # Angles in Segment
        text_16 = Tex(r"Angles in the same segment Theorem:").to_edge(UP).scale(1.2)
        text_17 = Tex(r"The theorem states that angle subtended by the same\\"
                      r"arc at the circumference are equal.", color=accent_color).to_edge(LEFT).shift(UP*2.1)
        text_group_2 = VGroup(
            Tex(r"Arc $CD$ subtends $\angle CAD$ and $\angle CBD$").scale(0.85),
            Tex(r"$\angle CBD = \angle CAD$ ($\angle$s subtended by same arc)").scale(0.85),
            Tex(r"$\angle CBD = \angle CAD = 26^\circ$").scale(0.85)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.75).move_to([2.25, -1, 0])
        self.play(FadeOut(text_14, text_15), ReplacementTransform(text_10, text_16), Write(text_group_2[0]),
                 circle_group.animate.to_edge(LEFT).shift(UP*0.5), FadeIn(text_17))
        self.play(AB.animate.set_color(main_color), angle_BAC.animate.set_opacity(0), angle_BAC_label.animate.set_opacity(0), AC.animate.set_color(BLUE_D),
                 BC.animate.set_color(BLUE_D), CD.animate.set_color(BLUE_D), BD.animate.set_color(BLUE_D),
                 angle_CBD.animate.set_opacity(1), arc_CD.animate.set_opacity(1))
        self.play(Flash(angle_CBD), Flash(angle_CAD), Indicate(arc_CD))
        self.wait()
        self.play(Write(text_group_2[1]))
        self.wait(0.5)
        self.play(arc_CD.animate.set_opacity(0), angle_CBD_label.animate.set_opacity(1), Indicate(angle_CAD), Indicate(angle_CBD))
        self.wait(0.5)
        self.play(Write(text_group_2[2]))
        self.wait(0.5)
        self.play(Flash(angle_CAD), Flash(angle_CBD), Indicate(angle_CAD_label), Indicate(angle_CBD_label))
        self.wait(3)

        # Final Answer
        text_18 = Tex(r"Calculate the Final Angle:").to_edge(UP).scale(1.2)
        text_19 = Tex(r"The angle we need to find, $\angle ABC$, is composed of two\\"
                      r"adjacent angles: $\angle ABD$ and $\angle CBD$", color=accent_color).to_edge(LEFT).shift(UP*2.3)
        text_20 = Tex(r"Final Answer:").to_edge(UP).scale(1.2)
        text_group_3 = VGroup(
            Tex(r"$\angle ABC = \angle ABD + \angle CBD$").scale(0.85),
            Tex(r"$\angle ABD = 90^\circ$ ($\angle$ in semicircle)").scale(0.85),
            Tex(r"$\angle ABC = 26^\circ + 90^\circ$").scale(0.85),
            Tex(r"$\angle ABC = 116^\circ$").scale(0.85)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.75).move_to([2.25, -1, 0])
        self.play(FadeOut(text_17, text_group_2), ReplacementTransform(text_16, text_18), Write(text_group_3[0]), FadeIn(text_19))
        self.wait(0.5)
        self.play(Write(text_group_3[1]))
        self.wait(0.5)
        self.play(angle_ABD.animate.set_stroke(opacity=1))
        self.play(Flash(angle_ABD))
        self.wait(0.5)
        self.play(Write(text_group_3[2]))
        self.wait(0.5)
        self.play(TransformFromCopy(text_group_3[2], text_group_3[3]))
        self.play(angle_ABC.animate.set_stroke(opacity=1),
                 angle_ABC_label.animate.set_opacity(1))
        self.wait(3)
        self.play(FadeTransform(text_18, text_20), text_group_3[3].animate.move_to(ORIGIN).shift(UP*1.5).scale(2),
                 circle_group.animate.move_to(ORIGIN).shift(DOWN*1.5), FadeOut(text_19, text_group_3[:3]))
        self.play(AD.animate.set_color(main_color), AC.animate.set_color(main_color), BC.animate.set_color(main_color), BD.animate.set_color(main_color),
                 angle_CAD.animate.set_opacity(0), angle_CBD.animate.set_opacity(0), angle_CAD_label.animate.set_opacity(0),
                 angle_CBD_label.animate.set_opacity(0), CD.animate.set_color(main_color), AC.animate.set_opacity(0), angle_DAB.animate.set_opacity(1),
                 angle_DAB_label.animate.set_opacity(1), angle_ABD.animate.set_opacity(0))
        self.wait(0.5)
        box = SurroundingRectangle(text_group_3[3], color=secondary_color)
        self.play(Indicate(circle_group), Indicate(text_group_3[3]))
        self.play(Create(box), text_20.animate.set_color(accent_color),
                 text_group_3[3].animate.set_color(accent_color))
        self.play(Flash(angle_ABC), Indicate(angle_ABC_label))
        self.wait(3)
        final_answer_group = VGroup(circle_group, box, text_20, text_group_3[3])
        self.play(ShrinkToCenter(final_answer_group))
        
        # Outro
        final_text = Tex("Thank you for watching!", color=accent_color).scale(1.5)
        self.play(Write(final_text))
        self.wait()
        self.play(logo_corner.animate.move_to(ORIGIN).scale(3), 
                  final_text.animate.to_edge(DOWN).set_color(text_color))
        self.wait(2)
        self.play(FadeOut(final_text, logo_corner))
        self.wait()