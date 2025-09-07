
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.cat([x1, 2 * x1], dim=-1)
        v2 = v1.view(v1.shape[0], -1)
        return torch.relu(v2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 4)
