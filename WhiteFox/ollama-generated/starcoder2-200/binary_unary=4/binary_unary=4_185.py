
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 64)

    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        if other is None:
            return v1
        else:
            v2 = v1 + other # Other tensor should be the argument of forward function
            return torch.relu(v2)

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(3, 32)
__output__  = m(x1, other=torch.randn(3, 64))
