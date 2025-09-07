
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1568627450980392):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
        self.negative_slope = negative_slope

    def forward(self, x):
        v1  = self.conv(x)
        mask  = v1 > 0
        v2  = v1 * (-0.5)
        v3  = torch.where(mask,v1, v2 )
        return v3

# Initializing the model
negative_slope= 1e-49
m  = Model(negative_slope)

# Inputs to the model
x1  = torch.randn(10, 8, 65, 65)
__output__  = m(x1)

