from typing import List
from enum import Enum

class ActionType(Enum):
    PRINT_TEXT = 1
    PRINT_IMAGE = 2

class Action:
    def __init__(self, type: ActionType, content: str):
        self.content = content
        self.type = type

    def do(self):
        return self.content

class ConditionType(Enum):
    CONTAINS = 1
    EQUALS = 2

class Condition:
    step = None
    condition_type: ConditionType
    condition_word: str

    def __init__(self, next_step, condition_type: ConditionType, word: str):
        self.step = next_step
        self.condition_type = condition_type
        self.condition_word = word

    def is_valid(self, input: str):
        if self.condition_type == ConditionType.CONTAINS:
            return self.condition_word.lower() in input.lower()
        elif self.condition_type == ConditionType.EQUALS:
            return self.condition_word.lower() is input.lower()
        else:
            return False

class Step:
    conditions: List[Condition]
    actions: List[Action]

    def __init__(self, actions):
        self.actions = actions
        self.conditions = []

    def add_condition(self, condition:Condition):
        self.conditions.append(condition)

    def do(self):
        res = []
        for a in self.actions:
            res.append(a.do())
        return res

class Scenario:
    steps: List[Step]

    def __init__(self, steps: List[Step]):
        self.steps = steps
        self.current_step = steps[0]

    def begin(self):
        return self.current_step.do()

    def is_finished(self):
        return len(self.current_step.conditions) == 0

    def check_connections(self, user_input:str):
        assert(self.current_step.conditions)

        for c in self.current_step.conditions:
            if c.is_valid(user_input):
                self.current_step = c.step

    def manage_display(self, user_input:str = None):
        self.check_connections(user_input)
        return self.current_step.do()
