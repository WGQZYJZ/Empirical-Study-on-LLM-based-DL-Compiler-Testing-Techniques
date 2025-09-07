
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(256, 8)
        self.relu = torch.nn.ReLU()

    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        if not isinstance(other, int):
            v3 = self.relu(v2 + other)
        else:
            v3 = 0
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 8)
y1 = m(x1)
y2 = m(x1, other=1)
