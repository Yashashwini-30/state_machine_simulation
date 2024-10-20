# state_machine_simulation
#using python
#State and Transition Definitions*
#The State class will represent each state, and the Transition class will represent the transitions between states based on inputs.
#- *Task*: Write code to define states and transitions.
class State:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Transition:
    def __init__(self, from_state, input_symbol, to_state):
        self.from_state = from_state
        self.input_symbol = input_symbol
        self.to_state = to_state 

 

