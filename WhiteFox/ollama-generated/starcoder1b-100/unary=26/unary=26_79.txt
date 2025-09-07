
class Model(torch.nn.Module):
    def __init__(self, negative_slope: float = 0.1):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        mask = x1 > 0
        v2 = torch.where(mask, x1, x1 * self.negative_slope)
        return v2


# Initializing the model
m = Model()


