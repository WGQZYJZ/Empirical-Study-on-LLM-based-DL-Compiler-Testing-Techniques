
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1, t2, t3):
        v1 = torch.cat([t1, t2, t3], dim=2)
        v2 = v1.view(...)
        v3 = torch.relu(v2)

        return v3


# Inputs to the model
x1 = torch.randn(1, 50, 28, 28)
x2 = torch.randn(1, 2000, 75000)
x3 = torch.randn(1, 256, 2048)
