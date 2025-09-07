
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 3, 5, stride=3, padding=1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        negative_slope = -0.1
        t1 = v1 > 0
        t3 = v1 * negative_slope
        t4 = torch.where(t1, v1, t3)
        return t4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 65536, 65536)
