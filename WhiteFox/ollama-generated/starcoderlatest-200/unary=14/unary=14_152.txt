
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(8, 3, 16, stride=16, padding=8)
 
    def forward(self, x1):
        v1 = self.conv_t(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 8, 64, 64)
