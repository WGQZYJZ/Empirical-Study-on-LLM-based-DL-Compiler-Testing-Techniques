
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 10, bias=False)

    def forward(self, x1):
        v1 = self.linear(x1) + 3  # The linear transformation does not affect the original value of x1.
        v2 = torch.clamp(v1, min=0, max=6, out=None) / 6
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3)
