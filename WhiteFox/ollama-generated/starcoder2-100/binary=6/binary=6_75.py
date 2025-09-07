
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other=0.5): # Add an input argument called 'other' with a default value of 0.5 for the argument
        v1 = self._linear(x1)
        v2 = v1 - other # This is the pattern
        return v2
 
    @staticmethod
    def _linear(v): 
        return torch.nn.Linear(784, 69)(v)
 
# Initializing the model
m  = Model()


# Inputs to the model