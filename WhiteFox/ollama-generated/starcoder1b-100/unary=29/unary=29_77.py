
class Model(torch.nn.Module):
    def __init__(self, min_value=-100., max_value=100.):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 4, stride=2, padding=1)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        return torch.clamp_min(v1, self.min_value), torch.clamp_max(v1, self.max_value)


# Initializing the model
m = Model()
x1 = torch.randn(3, 8, 64, 64)
min_value, max_value = -10., 10.
