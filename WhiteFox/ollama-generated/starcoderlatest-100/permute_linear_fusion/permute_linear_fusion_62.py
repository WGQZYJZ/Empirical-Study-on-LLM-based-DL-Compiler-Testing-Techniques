
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1.permute(0, 2, 1), ... ) # Apply linear transformation to the permuted tensor.
        return v1

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
