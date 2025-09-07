
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v = torch.cat([x1, x2], dim=0)
        v1 = v.view(-1, 4)
        v2 = torch.relu(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 2, 2)
x2 = torch.randn(5, 2, 2)
