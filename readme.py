# state_machine_simulation
#using python
#State and Transition Definitions*
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

  #- Create a class for the state machine.
  #- Add methods to add states and transitions.
  #- Set the initial state.
