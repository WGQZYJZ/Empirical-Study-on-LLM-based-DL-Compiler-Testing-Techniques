
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1): 
        v1 = torch.randn(32)
        v2  = self.linear(v1)
        v3  = other  # Value used in pattern
        v4  = v2 - v3
        v5  = torch.nn.functional.relu(v4)
        return v5


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 32) # Input tensor size depends on model, the model output is a vector of length 32
other = 0.54638709   # Value used in pattern


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3) * 0.5 + 0.5  # Input tensor size depends on model, the model output is a vector of length 3
other = -2.497869  # Value used in pattern

