
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 16, stride=4, padding=4)
        self.negative_slope = torch.nn.Parameter(torch.tensor(negative_slope))

    def forward(self, x1):
        v1 = self.conv_transpose(x1) > 0
        v2 = v1 * self.negative_slope
        v3 = torch.where(v1, v1, v2)
        return v3


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
