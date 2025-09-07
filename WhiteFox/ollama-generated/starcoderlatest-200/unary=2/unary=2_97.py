
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1024, 512, kernel_size=3, stride=1, padding=0)
        self.deconv = torch.nn.ConvTranspose2d(512, 1024, kernel_size=2, stride=2, output_padding=1)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.deconv(v1)
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x = torch.randn(64, 1024, 3, 32, 32)
