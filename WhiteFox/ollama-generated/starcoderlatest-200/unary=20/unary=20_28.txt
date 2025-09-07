
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 64, 1, stride=1, padding=0)
        self.trans_conv = torch.nn.ConvTranspose2d(64, 32, 4, stride=2, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.sigmoid(v1)
        v3 = self.trans_conv(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 64, 56, 70)
