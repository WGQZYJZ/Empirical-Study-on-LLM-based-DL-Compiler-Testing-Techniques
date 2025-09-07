
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = torch.mm(x1, x1)
        return torch.cat([v1, v1, ..., v1])


# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
