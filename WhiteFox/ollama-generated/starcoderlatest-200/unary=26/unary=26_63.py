
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 16, stride=2)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1) > 0
        v2 = v1 * negative_slope
        v4 = torch.where(v1, v2, v1)
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 3, 100, 76)
