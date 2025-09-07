
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2=None):
        v1 = None if (x1 is None or x2 is None) else (torch.nn.functional.linear(x1, ...))
        v2 = torch.nn.functional.linear(x2, ...)
        return v1 + v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 2)
