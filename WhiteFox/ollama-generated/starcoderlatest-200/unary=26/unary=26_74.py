
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_t  = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
        self.negative_slope = torch.nn.Parameter(
            torch.randn(self.conv_t.out_channels) * -0.05
        )
 
    def forward(self, x):
        v1 = self.conv_t(x)
        v2 = v1 > 0
        v3 = v1 * self.negative_slope[None]
        v4 = torch.where(v2, v1, v3)
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
