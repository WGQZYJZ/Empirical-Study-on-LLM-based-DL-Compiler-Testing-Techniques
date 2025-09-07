
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        torch.rand(...) # Use random function to generate a tensor filled with random numbers
        torch.randn(...).clamp_() # Use nanns function to generate an output in [-0.5, 0.5]
        torch.nn.functional.dropout(...) # Replace dropout function call
        return x1

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 3)
