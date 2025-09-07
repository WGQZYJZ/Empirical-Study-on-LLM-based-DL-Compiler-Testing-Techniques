
class Model(nn.Module):
    def __init__(self, negative_slope=0):
        super().__init__()
        self.negative_slope = negative_slope
        self.conv_transpose  = nn.ConvTranspose2d(3, 8, kernel_size=1, stride=1)
 
    def forward(self, x):
        v1 = self.conv_transpose(x)
        v2 = torch.where(v1 > 0, self.negative_slope * v1, 0)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
