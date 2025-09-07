
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(32, 8)
        self.linear2 = torch.nn.Linear(8, 4)

    def forward(self, x):
        return (x + self.linear1(x)) * self.linear2(x)


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 32)
y = torch.randn(1, 4)
