
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3):  # Only the first two inputs are used.
        return torch.split(x3, [10, 5], dim=0) + [1]


# Initializing the model
m = Model()


# Inputs to the model
__inputs__ = (torch.randn(2), torch.randn(1), torch.randn(2))
