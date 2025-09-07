
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 8)

    def forward(self, x1):
        l1 = self.linear(x1)
        return l5 + 3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 4, 64, 64)
