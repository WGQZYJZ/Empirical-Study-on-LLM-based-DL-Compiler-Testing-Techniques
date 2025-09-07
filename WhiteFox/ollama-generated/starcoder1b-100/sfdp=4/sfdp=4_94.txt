
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, mask=None):
        v1 = self.conv(x1)
        if mask is not None:
            output = v1 * math.exp(-mask)
        else:
            output = v1 * math.exp(-v1.pow(2).sum(-1).log() - 1)
        return output


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
mask = torch.rand(1, 50, 10, 10) > 0.5
