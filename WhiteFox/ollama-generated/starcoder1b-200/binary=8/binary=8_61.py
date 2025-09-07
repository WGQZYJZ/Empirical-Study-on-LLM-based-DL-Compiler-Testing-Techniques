
class Model(torch.nn.Module):
    def __init__(self, other_tensor):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, other):
        v1 = self.conv(x1) + other
        return v1


# Initializing the model
m = Model(torch.randn(1, 4))

