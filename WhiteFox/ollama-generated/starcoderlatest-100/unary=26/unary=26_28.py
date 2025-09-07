
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        t2 = v1 > 0
        v3 = v1 * self.negative_slope
        t4 = torch.where(t2, v1, v3)
        return t4


# Initializing the model
m = Model(-0.5)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
