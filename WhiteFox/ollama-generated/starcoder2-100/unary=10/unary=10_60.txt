

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.conv = torch.nn.Conv2d(3, 8, kernel_size=1)

    def forward(self, x):
        v0 = self.conv(x)
        v1 = v0 + 3
        v2 = torch.clamp_min(v1, min=-6.) / (-3.)
        v3 = torch.clamp_max(v2, max=59.) / (58. - 3. * 49.)

        return v3
