
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0)
        v2 = v1.view(-1)
        v3 = torch.relu(v2)
        return v3


# Initializing the model and creating inputs for it.
m  = Model()
x1 = torch.randn(1, 4, 4)
x2 = torch.randn(1, 4, 4)
