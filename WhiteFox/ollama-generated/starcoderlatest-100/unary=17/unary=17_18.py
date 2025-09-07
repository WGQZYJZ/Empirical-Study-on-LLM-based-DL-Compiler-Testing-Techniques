
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.deconv = torch.nn.ConvTranspose2d(8, 3, 4, stride=4, padding=0)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = F.relu(v1)
 
        v3 = self.deconv(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
