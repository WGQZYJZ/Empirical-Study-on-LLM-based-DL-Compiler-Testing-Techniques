
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.cat([x1[:, 0:3], x1[:, 2]], dim=1)
        return torch.relu(v)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 4)  # Input data
