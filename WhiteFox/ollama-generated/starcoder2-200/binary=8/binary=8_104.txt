
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x):
        v1 = self.conv(x)

        # This is a new keyword argument that is passed as an argument to the addition operation.
        self._other_tensor  = torch.randn(v1.size())
        return v1 + other

m = Model()

