
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(x1, x2):
        v1 = torch.cat([x1, x2], dim=2)
        v2 = v1.view(v1.size()[0], -1)
        v3 = torch.nn.functional.relu(v2)
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 2, 2)
x2 = torch.randn(2, 2, 2)
