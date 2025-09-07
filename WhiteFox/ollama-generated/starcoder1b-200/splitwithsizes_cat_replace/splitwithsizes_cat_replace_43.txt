
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        s1 = torch.split(x1, 3, dim=0)
        c = torch.cat([s1[i] for i in range(3)], dim=0)
        return c


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 8, 8)
