Team 2 task is to implement the state machine simulation logic

class StateMachine:
    def _init_(self, states, transitions, initial_state):
        """
        Initialize the state machine with possible states, transitions, and initial state.
        
        states: list of all possible states
        transitions: dictionary of transitions, e.g., 
                     { 'state1': {'input1': 'state2', 'input2': 'state3'}, ... }
        initial_state: the state from which the machine starts
        """
        self.states = states
        self.transitions = transitions
        self.current_state = initial_state

    def transition(self, input_value):
        """
        Handle an input and move to the next state based on the current state and input.
        """
        if input_value in self.transitions[self.current_state]:
            next_state = self.transitions[self.current_state][input_value]
            print(f"Transitioning from {self.current_state} to {next_state} on input {input_value}")
            self.current_state = next_state
        else:
            print(f"No transition found for input {input_value} in state {self.current_state}")

    def get_current_state(self):
        """
        Return the current state of the machine.
        """
        return self.current_state
