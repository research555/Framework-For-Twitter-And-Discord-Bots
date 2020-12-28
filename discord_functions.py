from asyncio import sleep
import random
from collections import deque

def RemoveTupleFromHandles(handles):
    # SQL results are pulled as tuples. Run the code below to make them into strings

    converted_handles = []
    list_to_deque = deque(handles)

    for values in handles:
        popped_item = list_to_deque.popleft()
        if type(popped_item) is tuple:
            tup_to_str = ''.join(popped_item)
            converted_handles.append(tup_to_str)
        else:
            converted_handles.append(popped_item)

    return converted_handles

def VariousLongText(assignment, handles):

    no_match_id_txt = "```There doesn't seem to be a Tweet ID matching the one you just sent me, are you sure you have entered the correct ID?```"

    no_match_major_txt = f"```Unfortunately, the major '{assignment}' does not currently exist on our database. Are you sure you typed it in correctly?\n\n"\
                         f"To view all of our current majors, please use the command .showallmajors in the #database channel.```"

    success_assignment_1_txt = f'```Woo! You have successfully assigned {handles[1]}, who is an expert in {assignment}.\n\n'\
                           f'Bear in mind, this is our only expert in {assignment}, so maybe think twice about assigning him again soon!\n\n'\
                           f'If you think you have made a mistake, please react to this message within one minute!```'

    appending_mentor_failure_txt = f'```There has been an issue appending the mentors to the assigned_mentors table. ' \
            f'Please review error log on #errors\n\n' \
            f'The length of [handles] is {len(handles)}. This should always be either 3 or 4\n' \
            f'it currently looks like this {handles}.```'

    return no_match_id_txt, no_match_major_txt, success_assignment_1_txt, appending_mentor_failure_txt