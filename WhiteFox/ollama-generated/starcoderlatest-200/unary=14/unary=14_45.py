
class GLULayer(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(16, 48, 3, stride=2, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        return v3


# Initializing the model
m = GLULayer()

# Inputs to the model
x1 = torch.randn(8, 48, 64, 64)
