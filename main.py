from interface.communication import Chat, ChatMode
from processing.scenario import Scenario, Action, Condition, ConditionType, Step, ActionType
import argparse

action1 = Action(content="How are you?", type=ActionType.PRINT_TEXT)
action2 = Action(content="Why ?", type=ActionType.PRINT_TEXT)
action3 = Action(content="Cool !", type=ActionType.PRINT_TEXT)
action4 = Action(content="Here's something to brighten your day =>", type=ActionType.PRINT_TEXT)
action5 = Action(content="(sending image: https://tinybuddha.com/blog/the-secret-that-laid-back-always-happy-guy-knows-that-you-dont/)", type=ActionType.PRINT_IMAGE)

step1 = Step([action1])
step2 = Step([action2])
step3 = Step([action3])
step4 = Step([action4, action5])

cond2 = Condition(next_step=step2, condition_type=ConditionType.CONTAINS, word="sad")
cond3 = Condition(next_step=step3, condition_type=ConditionType.CONTAINS, word="fine")
cond4 = Condition(next_step=step4, condition_type=ConditionType.CONTAINS, word="day")

step1.add_condition(cond2)
step1.add_condition(cond3)
step2.add_condition(cond4)

scenario = Scenario([step1, step2, step3, step4])

parser = argparse.ArgumentParser(description='Switch bot interface.')
parser.add_argument("--http", type=int, nargs='?',const=True, default=0, help="Activate nice mode.")
args = parser.parse_args()

chat = Chat([scenario], ChatMode.HTTP if args.http==1 else ChatMode.CLI)
chat.interact()