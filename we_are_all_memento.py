from manimlib import *

class WeAreAllMemento(Scene):
    def construct(self):
        # Create the goal
        goal = Text("Goal").to_edge(RIGHT)
        self.play(Write(goal))

        # Create the path
        path = Line(LEFT*5, RIGHT*5).shift(DOWN)
        self.play(ShowCreation(path))

        # Create the character
        character = Dot(LEFT*5 + DOWN)
        self.play(FadeIn(character))

        # Move the character towards the goal
        self.play(character.animate.move_to(LEFT*2 + DOWN), run_time=2)

        # Introduce distractions
        distractions = [
            Text("Emotional Aversion").scale(0.5).move_to(UP*2 + LEFT*1),
            Text("Impostor Syndrom").scale(0.5).move_to(UP*1 + LEFT*3),
            Text("Burnout").scale(0.5).move_to(UP*2 + RIGHT*1)
        ]
        for distraction in distractions:
            self.play(FadeIn(distraction))

        # Character gets distracted
        self.play(character.animate.move_to(distractions[0].get_center()), run_time=2)
        self.wait(1)
        # Character forgets the goal
        self.play(FadeOut(goal), FadeOut(path))
        self.wait(1)


### **B. "Monkey Branch to Branch" Metaphor**


class MonkeyBranchToBranch(Scene):
    def construct(self):
        # Create branches
        branches = []
        for x in range(-5, 6, 2):
            branch = Line(UP*2, DOWN*2).shift(RIGHT*x)
            branches.append(branch)
            self.play(ShowCreation(branch))

        # Create the monkey (use a Dot as a placeholder)
        monkey = Dot(branches[0].get_top(), color=ORANGE)
        self.play(FadeIn(monkey))

        # Animate the monkey swinging
        for i in range(len(branches)-1):
            start_point = branches[i].get_top()
            end_point = branches[i+1].get_top()
            arc = ArcBetweenPoints(start_point, end_point, angle=PI/2)
            self.play(MoveAlongPath(monkey, arc), run_time=1.5)
            self.wait(0.5)


### **C. "The String" Concept**


class TheStringConcept(Scene):
    def construct(self):
        # Create branches
        branches = []
        for x in range(-5, 6, 2):
            branch = Line(UP*2, DOWN*2).shift(RIGHT*x)
            branches.append(branch)
            self.play(ShowCreation(branch))

        # Create the string
        string_points = [branch.get_top() for branch in branches]
        string = VMobject()
        string.set_points_smoothly(string_points)
        string.set_color(RED)
        self.play(ShowCreation(string))

        # Move the monkey along the string
        monkey = Dot(branches[0].get_top(), color=ORANGE)
        self.play(FadeIn(monkey))
        self.play(MoveAlongPath(monkey, string), run_time=5)


### **D. Environmental Design Principles**


class EnvironmentalDesignPrinciples(Scene):
    def construct(self):
        # Scenario 1: Cluttered Environment
        clutter = VGroup(*[
            Square(side_length=0.5, color=GREY).move_to(np.array([np.random.uniform(-5, 5), np.random.uniform(-3, 3), 0]))
            for _ in range(20)
        ])
        self.play(FadeIn(clutter))
        self.wait(1)

        # Character tries to move through clutter
        character = Dot(LEFT*5 + DOWN*2, color=BLUE)
        self.play(FadeIn(character))
        self.play(character.animate.move_to(RIGHT*5 + UP*2), run_time=5, rate_func=linear)
        self.wait(1)

        # Scenario 2: Designed Environment
        self.play(FadeOut(clutter))
        path = Line(LEFT*5 + DOWN*2, RIGHT*5 + UP*2, color=GREEN)
        self.play(ShowCreation(path))
        self.play(character.animate.move_to(LEFT*5 + DOWN*2), run_time=1)
        self.play(MoveAlongPath(character, path), run_time=5)
        self.wait(1)


### **E. Feedback Loops and Course Correction**


class FeedbackLoops(Scene):
    def construct(self):
        # Create the intended path
        path = Line(LEFT*5, RIGHT*5, color=GREEN)
        self.play(ShowCreation(path))

        # Character starts on the path
        character = Dot(LEFT*5, color=PURPLE)
        self.play(FadeIn(character))

        # Character deviates
        deviation = UP*3
        self.play(character.animate.move_to(LEFT*2 + deviation), run_time=2)

        # Feedback mechanism appears
        feedback = Arrow(character.get_center(), path.point_from_proportion(0.3), color=YELLOW)
        feedback_text = Text("Adjust Course").scale(0.5).next_to(feedback, UP)
        self.play(ShowCreation(feedback), Write(feedback_text))

        # Character returns to path
        self.play(character.animate.move_to(path.point_from_proportion(0.3)), run_time=2)
        self.wait(1)

