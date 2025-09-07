

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32*32*3, 512)

    def forward(self, x):
        v0 = self.linear(x)
        return torch.sigmoid(v0)

# Initializing the model
m = Model()

# Inputs to the model
v0 = torch.randn(64, 32*32*3)
__output__  = m(v0)

