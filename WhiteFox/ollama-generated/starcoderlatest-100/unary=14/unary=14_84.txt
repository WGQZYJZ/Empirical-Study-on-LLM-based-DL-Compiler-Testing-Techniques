
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 16, 4, stride=2, padding=1)
        self.conv_transpose = torch.nn.ConvTranspose2d(16, 8, 4, stride=2, padding=0)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        v4 = self.conv_transpose(v3)
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 3, 64, 64)
