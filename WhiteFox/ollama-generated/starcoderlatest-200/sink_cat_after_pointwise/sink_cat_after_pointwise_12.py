
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v = torch.cat([x1, x2], dim=0)
        return self.relu(v)

    def relu(self, t):
        return torch.relu(t)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 4)
x2 = torch.randn(2, 4, 5)
