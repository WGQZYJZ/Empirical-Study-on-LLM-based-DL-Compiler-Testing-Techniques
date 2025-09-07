
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 8, 1, stride=2, output_padding=0) 
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        t1 = v1 > 0
        v3 = self.conv_transpose(v1 * self.negative_slope)
        v4 = torch.where(t1, v1, v3) 
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(256, 3, 64, 64)
