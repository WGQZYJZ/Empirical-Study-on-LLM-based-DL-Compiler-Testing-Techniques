
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.ConvTranspose2d(3, 8, kernel_size=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) > 0
        v2 = x1 * -1
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 8, 64, 64)
