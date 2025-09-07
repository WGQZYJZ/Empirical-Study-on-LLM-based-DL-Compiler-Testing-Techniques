
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        mask = v1 > 0
        negative_slope = torch.nn.Parameter(torch.zeros(1), requires_grad=False).fill_(negative_slope)
        v2 = v1 * negative_slope

        