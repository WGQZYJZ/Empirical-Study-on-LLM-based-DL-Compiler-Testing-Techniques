
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(3, 8)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * clamp(min=0, max=6, v1 + 3)
        v4 = v2 / 6
        return v4


m = Model()


# Inputs to the model
x1 = torch.randn(1, 3)
