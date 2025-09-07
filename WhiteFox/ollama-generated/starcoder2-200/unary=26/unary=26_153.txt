
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 > 0

        neg_slope = -0.7
        negative_v3  = v1 * neg_slope
        v4 = torch.where(v2, v1, negative_v3)
 
        return v4


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(100, 3, 650, 890)
__output__  = m(x1)