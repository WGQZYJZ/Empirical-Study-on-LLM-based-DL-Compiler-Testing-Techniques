
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1 = torch.tensor([0])): # Initialize the model with an input tensor y1 to this forward function.
        v2  = self._linear(x1) + y1 
        v3  = self._relu(v2) 
        return v3

    def _linear(self, x):
        return (torch.ones_like(x) * 0.)
    
    def _relu(self, x): # Implement the ReLU function here for the user.
        return torch.nn.functional.relu(x)

# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(456320, 897)
 
