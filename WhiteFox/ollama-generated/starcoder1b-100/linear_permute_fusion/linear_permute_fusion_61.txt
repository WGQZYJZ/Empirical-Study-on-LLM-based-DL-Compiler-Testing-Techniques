
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 4)

    def forward(self, x1):
        v2 = self.linear(x1)
        return v2


# Inputs to the model
x1 = torch.randn(1, 2, 3, 4)
