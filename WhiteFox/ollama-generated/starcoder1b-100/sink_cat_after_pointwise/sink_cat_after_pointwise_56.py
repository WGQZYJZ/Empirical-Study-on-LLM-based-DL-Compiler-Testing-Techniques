
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3):  # Forward propagation
        v1 = torch.cat([x1, x2, x3], dim=2)
        v2 = torch.relu(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 4)
x2 = torch.randn(1, 5)
x3 = torch.randn(1, 2)
