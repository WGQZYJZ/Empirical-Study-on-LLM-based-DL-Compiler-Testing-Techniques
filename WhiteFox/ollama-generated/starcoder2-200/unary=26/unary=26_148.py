
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv = torch.nn.ConvTranspose1d(3, 8, 4)
        self.negative_slope  = negative_slope

    def forward(self, x1):
        v1  = self.conv(x1)

        mask = (v1 > 0).detach()

        v2  = -self.negative_slope*mask * v1
        v3  = torch.where(mask, v1, v2)
        return v3


# Initializing the model
m = Model(negative_slope=0.2569483747768402)

# Inputs to the model
x1 = torch.randn(1, 3, 128)

__output__  = m(x1)

