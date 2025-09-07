
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(...)

    def forward(self, x1):
        v1 = ...  # Generate a random input with arbitrary shape
        v2 = self.linear(v1)
        return v2


# Input to the model
x1 = torch.randn(1, ...)  # Permute input of the model from (..., ...) to (, ...).
