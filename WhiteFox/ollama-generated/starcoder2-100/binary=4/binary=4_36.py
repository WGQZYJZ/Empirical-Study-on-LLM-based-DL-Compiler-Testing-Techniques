
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, 42) # Apply the linear transformation with bias=False to the input tensor
        v2 = v1 + other
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(10, 8)
other = torch.randn(8).long() # Add another random tensor of the same size as x1
__output__  = m(x1)
