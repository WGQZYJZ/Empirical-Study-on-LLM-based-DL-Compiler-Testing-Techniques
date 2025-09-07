
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.cat([x1, x2, ...], dim=1)
        v2 = v1.view(...)
        return torch.relu(v2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 64, 80)
x2 = torch.randn(1, 3, 50)
