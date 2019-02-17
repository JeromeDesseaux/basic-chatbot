from processing.scenario import Scenario, Condition
from typing import List
from enum import Enum

class ChatMode(Enum):
    CLI = 1
    HTTP = 2

class Chat():
    scenarii = List[Scenario]
    mode: ChatMode
    current_scenario: Scenario

    def __init__(self, scenarii: List[Scenario], mode=ChatMode.CLI):
        self.scenarii = scenarii
        self.current_scenario = None
        self.mode = mode

    def bot_print(self, to_print:List[str]):
        for s in to_print:
            if self.mode is ChatMode.HTTP:
                print("(sending HTTP request: {'text':"+s+"}")
            else:
                print("Bot> "+s)


    def interact(self):
        response = self.read_input()
        fallback = self.set_current_scenario(response)
        while not fallback:
            response = self.read_input()
            fallback = self.set_current_scenario(response)
        self.bot_print(self.current_scenario.begin())
        loop = True
        while loop:
            try:
                response = self.read_input()
                disp = self.current_scenario.manage_display(response)
                if len(disp) is 0:
                    self.fallback()
                else:
                    self.bot_print(disp)
            except Exception as e:
                self.bot_print(['Ohoh, an error just occured'])
                break
            finally:
                loop = not self.current_scenario.is_finished()
        self.bot_print(["It's been a pleasure! See you soon :D"])

    def fallback(self):
        self.bot_print(["Sorry I don't understand."])
    
    def read_input(self):
        return input("ME> ")

    def set_current_scenario(self, input:str):
        if 'hello' in input.lower():
            self.current_scenario = self.scenarii[0]
            return True
        else:
            self.fallback()
            return False