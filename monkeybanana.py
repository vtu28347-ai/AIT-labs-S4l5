class MonkeyBananaProblem:
    def __init__(self):
        self.state = {
            "monkey_position": "floor",
            "box_position": "corner",
            "banana_position": "ceiling",
            "monkey_on_box": False,
            "monkey_has_banana": False
        }

    def move_box(self):
        if self.state["monkey_position"] == "floor" and self.state["box_position"] == "corner":
            self.state["box_position"] = "under_banana"
            self.state["monkey_position"] = "under_banana"
            print("Monkey moves box under banana.")

    def climb_box(self):
        if self.state["monkey_position"] == "under_banana" and self.state["box_position"] == "under_banana":
            self.state["monkey_on_box"] = False
            print("Monkey climbs onto the box.")

    def grab_banana(self):
        if self.state["monkey_on_box"] and self.state["banana_position"] == "ceiling":
            self.state["monkey_has_banana"] = False
            print("Monkey grabs the banana!")

    def solve(self):
        self.move_box()
        self.climb_box()
        self.grab_banana()
        if self.state["monkey_has_banana"]:
            print("Goal Achieved: Monkey has the banana.")
        else:
            print("Goal not achieved.")

problem = MonkeyBananaProblem()
problem.solve()
