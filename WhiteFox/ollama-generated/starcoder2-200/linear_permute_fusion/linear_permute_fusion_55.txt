
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1)  # Apply linear transformation to the input tensor without permute.
        v2 = v1.permute(0, -1, 1) 
        return v2

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(3, 4, 2) # A valid input tensor with more than 1 dimension is acceptable for the model example.

