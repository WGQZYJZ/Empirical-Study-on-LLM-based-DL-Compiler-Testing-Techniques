
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        y  = torch.cat([x1, x1], dim=0)  # Concatenation of the input tensors along a specified dimension
        return y


# Inputs to the model
x1 = torch.randn(4, 3)   # Input tensor for the first layer
x2 = torch.randn(3, 6)   # Input tensor for the second layer
