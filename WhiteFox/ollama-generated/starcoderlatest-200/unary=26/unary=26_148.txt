
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 5, stride=2, padding=3)
        self.conv_transpose = torch.nn.ConvTranspose2d(in_channels=8, out_channels=8, kernel_size=10, stride=4, padding=5)
        self.sigmoid = torch.nn.Sigmoid()
 
    def forward(self, x):
        v1 = self.conv_transpose(x)
        v2 = v1 > 0
        v3 = v1 * self.negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4


# Initializing the model with a negative slope of -0.1
m = Model(negative_slope=-0.1)

# Input to the model
x = torch.randn(8, 3, 64, 64)
