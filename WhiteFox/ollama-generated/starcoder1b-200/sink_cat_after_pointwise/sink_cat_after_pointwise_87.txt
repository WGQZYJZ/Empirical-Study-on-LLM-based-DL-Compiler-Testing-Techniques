
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2=None):
        if x2 is not None:
            v1 = x1 + x2
        else:
            v1 = x1
        v2 = torch.relu(self.linear(v1))
        return v2


# Inputs to the model
x1 = torch.randn(1, 2, 2)
