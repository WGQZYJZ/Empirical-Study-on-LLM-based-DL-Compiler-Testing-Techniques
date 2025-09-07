
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, ...):  # Only the input argument of the `forward` method can change
        ...
        return x2


# Input to the model
x1 = torch.randn(...)
x2 = torch.randn(...)
