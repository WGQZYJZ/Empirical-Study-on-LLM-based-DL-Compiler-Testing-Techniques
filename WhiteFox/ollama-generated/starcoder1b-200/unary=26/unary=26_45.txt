
class Model(nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.negative_slope = negative_slope

    def forward(self, x1):
        v1 = conv_transpose(x1)
        v2 = torch.where(v1 > 0, v1 * self.negative_slope, v1 * -1)
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
