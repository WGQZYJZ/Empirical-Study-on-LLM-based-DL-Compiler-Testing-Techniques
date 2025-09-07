
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 16, 4, stride=2)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        negative_slope = -1
        v2 = torch.where(v1 > 0, v1, negative_slope * v1)
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 56, 80)
