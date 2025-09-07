
class Model(torch.nn.Module):
    def __init__(self, max=10., min=-5.):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x):
        v1  = self.conv(x)
        v2  = torch.clamp_min(v1, min=-5.) # Clamp the output of the convolution to a minimum value (-5)
        v3  = torch.clamp_max(v2, max=10.) # Clamp the output of the previous operation to a maximum value (10)

        return v3


m  = Model()
x1  = torch.randn(1, 3, 64, 64)
