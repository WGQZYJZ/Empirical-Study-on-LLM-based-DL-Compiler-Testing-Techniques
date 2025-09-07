
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.cat([x1, x1], dim=2)
        v2 = torch.nn.functional.linear(v1, ...) # Apply linear transformation to the concatenated tensor.
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 3)
