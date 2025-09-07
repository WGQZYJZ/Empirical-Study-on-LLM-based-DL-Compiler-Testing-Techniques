
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_t  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
        self.negative_slope = -0.5
 
    def forward(self, x1):
        v1 = self.conv_t(x1) > 0
        v2 = v1 * self.negative_slope
        v3 = torch.where(v1 == True, v2, v1)
        return v3


# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
