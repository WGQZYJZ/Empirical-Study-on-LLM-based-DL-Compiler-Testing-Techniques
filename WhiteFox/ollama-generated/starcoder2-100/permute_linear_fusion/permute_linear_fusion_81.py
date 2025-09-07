
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1) # Apply linear transformation to the permuted tensor.
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 4, 5)


# Initializing the model