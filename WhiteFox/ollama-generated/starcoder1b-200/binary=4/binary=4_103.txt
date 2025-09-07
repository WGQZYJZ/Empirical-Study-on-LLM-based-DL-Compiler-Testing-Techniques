
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(32, 4)
        self.linear2 = torch.nn.Linear(4, 4)

    def forward(self, x):
        return self.linear1(x) + self.linear2(x)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 32)
