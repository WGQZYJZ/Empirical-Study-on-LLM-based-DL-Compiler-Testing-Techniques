
class GLUModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(1, 8, 4, stride=2, padding=1)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        return v3


# Initializing the model
m = GLUModel()

# Inputs to the model
x = torch.randn(1, 1, 64, 64)
