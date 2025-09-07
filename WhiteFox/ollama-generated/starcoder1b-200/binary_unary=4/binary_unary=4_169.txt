
class Model(torch.nn.Module):
    def __init__(self, other=1):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)
        self.relu  = torch.nn.ReLU()
        self.other = other

    def forward(self, x1):
        return self.linear(x1 + self.other), self.relu(x1)


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(2, 3)
__output__, __error_vec__ = m(x1)


