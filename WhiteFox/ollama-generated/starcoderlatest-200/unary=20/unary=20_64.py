
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(16, 32, kernel_size=4, stride=2)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.sigmoid(v1)
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(4, 16, 32, 32)
