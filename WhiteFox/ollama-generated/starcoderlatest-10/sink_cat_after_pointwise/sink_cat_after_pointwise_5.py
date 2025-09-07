
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 1)
        self.relu = torch.nn.ReLU()

    def forward(self, x):
        y = torch.cat([x, x], dim=0)
        z = y.view(4, -1)
        w = self.relu(z)
        return w

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 2, 3)
