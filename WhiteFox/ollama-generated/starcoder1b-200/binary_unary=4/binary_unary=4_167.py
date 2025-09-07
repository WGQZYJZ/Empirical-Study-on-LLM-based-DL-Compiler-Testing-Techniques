
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(3, 10)
        self.relu   = torch.nn.ReLU()
        self.other  = other

    def forward(self, x1):
        v1 = self.linear(x1) + self.other
        return self.relu(v1)


# Initializing the model
m = Model(1)


# Inputs to the model
x1 = torch.randn(2, 3)
