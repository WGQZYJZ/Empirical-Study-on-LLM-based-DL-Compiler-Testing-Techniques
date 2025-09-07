
class Model2(torch.nn.Module):
    def __init__(self, num_channels=16, kernel_size=3):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(num_channels, num_channels, kernel_size, stride=2, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        return v3


# Initializing the model
m2 = Model2()

 # Inputs to the model
x2 = torch.randn(1, 16, 4096, 784)
