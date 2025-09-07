
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8)
        self.linear2 = torch.nn.Linear(8, 4)

    def forward(self, x):
        l1  = self.linear1(x)
        l2  = self.linear2(l1 + 3)
        return l2 / 6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3)
