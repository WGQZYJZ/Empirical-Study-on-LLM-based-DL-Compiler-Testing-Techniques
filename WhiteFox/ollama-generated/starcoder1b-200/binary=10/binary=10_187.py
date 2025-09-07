
class Model(torch.nn.Module):
    def __init__(self, other=1000):
        super().__init__()
        self.linear = torch.nn.Linear(3, 6)

    def forward(self, x):
        y = self.linear(x)
        z = torch.add(y, other)
        return z


# Initializing the model
m = Model()

