
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(16, 32, 5, stride=2, padding=2)
 
    def forward(self, x2):
        v2 = self.conv(x2)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x2 = torch.randn(1, 32, 64, 64)
