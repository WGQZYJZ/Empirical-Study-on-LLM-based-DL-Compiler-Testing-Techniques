
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.125):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(8, 3, kernel_size=4, stride=2)
        self.neg_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv_t(x1)
        v2 = v1 > 0
        v3 = v1 * self.neg_slope
        v4 = torch.where(v2, v1, v3)
        return v4


# Initializing the model
m = Model()

 # Inputs to the model
 x1 = torch.randn(1, 8, 16, 16)
 