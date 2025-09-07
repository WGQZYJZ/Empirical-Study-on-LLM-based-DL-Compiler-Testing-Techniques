
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_up = torch.nn.ConvTranspose2d(4096, 16384, kernel_size=4, stride=2, padding=1)
        self.conv   = torch.nn.Conv2d(16384, 16384, kernel_size=4, stride=2, padding=1)
 
    def forward(self, x1):
        v1 = self.conv_up(x1)
        v2 = v1 * torch.sigmoid(self.conv(v1))
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 16384, 64, 64)
