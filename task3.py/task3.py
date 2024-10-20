Input Sample 1: Basic Sequence
python
Copy code
# Input sequence 1: Basic transitions between states
input_sequence_1 = ["input_1", "input_2", "input_1", "input_1"]
Starts in the default IDLE state.
The first input_1 moves the state from IDLE to WORKING.
The second input_2 moves the state from WORKING to PAUSED.
The third input_1 returns the state to WORKING.
The fourth input_1 moves it back to IDLE.
# Sample state machine definition (assuming states and transitions are already defined)
class StateMachine:
    def _init_(self):
        # Define states and transitions in a dictionary format
        self.states = {
            "IDLE": {"input_1": "WORKING", "input_2": "IDLE"},
            "WORKING": {"input_1": "IDLE", "input_2": "PAUSED"},
            "PAUSED": {"input_1": "WORKING", "input_2": "IDLE"}
        }
        self.current_state = "IDLE"  # Initial state
    
    def transition(self, input_signal):
        # Check for transition based on input signal
        if input_signal in self.states[self.current_state]:
            self.current_state = self.states[self.current_state][input_signal]
        else:
            print(f"No transition defined for input: {input_signal} in state: {self.current_state}")
        return self.current_state

# Create a state machine instance
sm = StateMachine()

# Define sample input sequences
input_sequences = ["input_1", "input_2", "input_2", "input_1", "input_1"]

# Simulate the state transitions based on input sequences
for input_signal in input_sequences:
    new_state = sm.transition(input_signal)
    print(f"After input {input_signal}: Current state is {new_state}")