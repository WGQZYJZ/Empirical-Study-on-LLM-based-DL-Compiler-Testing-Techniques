
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 3, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return torch.sigmoid(v1)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 8, 64, 64)
