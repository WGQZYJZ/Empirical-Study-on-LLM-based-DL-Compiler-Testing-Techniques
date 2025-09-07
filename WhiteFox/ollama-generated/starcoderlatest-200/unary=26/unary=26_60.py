
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = (v1 > 0).float() * negative_slope
        v3 = torch.where(v2, v1, v1 - 1)
        return v3


# Initializing the model
m = Model(-1)

 # Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
