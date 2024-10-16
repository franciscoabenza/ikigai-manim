from manimlib import *
import numpy as np
import os

# lets interveen here with an interactive ipython


class GolgiWall(VGroup):
    def __init__(self, num_curves=5, curve_height=4, curve_width=0.5, **kwargs):
        super().__init__(**kwargs)
        self.num_curves = num_curves
        self.curve_height = curve_height
        self.curve_width = curve_width
        self.create_wall()

    def create_wall(self):
        for i in range(self.num_curves):
            curve = CubicBezier(
                a0=np.array([-2, -self.curve_height/2, 0]),
                h0=np.array([-2+self.curve_width, -self.curve_height/2, 0]),
                h1=np.array([-2+self.curve_width, self.curve_height/2, 0]),
                a1=np.array([-2, self.curve_height/2, 0])
            )
            self.add(curve)
            self.shift(RIGHT * 0.5)  # Adjust spacing between curves
        
        self.set_stroke(color=RED, width=2)
        self.move_to(ORIGIN)  # Move to the left of the screen

class IkigaiDiagram(Scene):
    def construct(self):
        # Define colors for each circle
        color_love = BLUE_E
        color_good_at = GREEN_E
        color_world_needs = RED_E
        color_paid_for = YELLOW_E

        # Create circles with transparency to show overlaps
        circle_love = Circle(radius=2, fill_color=color_love, fill_opacity=0.5, stroke_color=color_love).shift(UP*1.2)
        circle_good_at = Circle(radius=2, fill_color=color_good_at, fill_opacity=0.5, stroke_color=color_good_at).shift(LEFT*1.2)
        circle_world_needs = Circle(radius=2, fill_color=color_world_needs, fill_opacity=0.5, stroke_color=color_world_needs).shift(DOWN*1.2)
        circle_paid_for = Circle(radius=2, fill_color=color_paid_for, fill_opacity=0.5, stroke_color=color_paid_for).shift(RIGHT*1.2)

        
        # Labels for each circle
        label_love = Text("What you\nlove", color=WHITE).scale(0.6).next_to(circle_love, UP, buff=0.3)
        label_good_at = Text("What you\nare good at", color=WHITE).scale(0.6).next_to(circle_good_at, LEFT, buff=0.3)
        label_world_needs = Text("What the\nworld needs", color=WHITE).scale(0.6).next_to(circle_world_needs, DOWN, buff=0.3)
        label_paid_for = Text("What you\ncan be paid for", color=WHITE).scale(0.6).next_to(circle_paid_for, RIGHT, buff=0.3)

        
       
        # # Add this line to enter interactive mode after circles are drawn
        # self.embed()
        
        # # Overlapping area labels
        # passion = Text("Passion", color=WHITE).scale(0.7).move_to(circle_love.get_bottom() + circle_good_at.get_right() + UP * 0.5 + RIGHT * 0.5)
        # mission = Text("Mission", color=WHITE).scale(0.7).move_to(circle_love.get_bottom() + circle_world_needs.get_top() + DOWN * 0.5)
        # vocation = Text("Vocation", color=WHITE).scale(0.7).move_to(circle_world_needs.get_right() + circle_paid_for.get_left() + LEFT * 0.5)
        # profession = Text("Profession", color=WHITE).scale(0.7).move_to(circle_good_at.get_bottom() + circle_paid_for.get_left() + UP * 0.5 + LEFT * 0.5)
        
        # Central Ikigai label
        ikigai = Text("IKIGAI", color=WHITE).scale(1).move_to(ORIGIN)


        # Animate text transforming into circles
        self.play(Write(label_love))
        self.play(Transform(label_love, circle_love))
        self.play(Write(label_good_at))
        self.play(Transform(label_good_at, circle_good_at))
        self.play(Write(label_world_needs))
        self.play(Transform(label_world_needs, circle_world_needs))
        self.play(Write(label_paid_for))
        self.play(Transform(label_paid_for, circle_paid_for))

        golgi_wall = GolgiWall()

        # Calculate the deepest overlap (Ikigai)
        ikigai_core = Intersection(
            Intersection(circle_love, circle_good_at),
            Intersection(circle_world_needs, circle_paid_for)
        )
        ikigai_core.set_fill(WHITE, opacity=1)
        ikigai_core.set_stroke(WHITE, width=2)
        
        # I want to glow ikigai_core
        
        
        ikigai_core.move_to(ORIGIN).shift(OUT * 1)  # Move up in the z-direction

        # Duplicate ikigai_core and add depth
        ikigai_core_duplicate = ikigai_core.copy()
        ikigai_core_duplicate.set_fill(WHITE, opacity=1)
        ikigai_core_duplicate.set_stroke(WHITE, width=2)
        ikigai_core_duplicate.thickness = 0.5  # Example property to add depth; replace with appropriate Manim method

        # Transform the original ikigai_core to the thickened version
        self.play(Transform(ikigai_core, ikigai_core_duplicate))

        # Animate the overlapping area
        self.play(FadeIn(ikigai_core))
        self.play(ikigai_core.animate.shift(OUT * 0.5))  # Adjust the distance as needed

        # Animate overlapping area labels
        # self.play(Write(passion))
        # self.play(Write(mission))
        # self.play(Write(profession))
        # self.play(Write(vocation))

        # Animate IKIGAI label at the center
        self.play(Write(ikigai))

        # Create and animate the Golgi wall
        # self.play(FadeIn(golgi_wall))

        self.wait(2)


if __name__ == "__main__":
    os.system("manimgl IkigaiDiagram.py IkigaiDiagram")