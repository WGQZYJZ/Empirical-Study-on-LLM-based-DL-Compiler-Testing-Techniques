
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(1, 4, kernel_size=4, stride=4, padding=0, output_padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp(v1, min=-10.0, max=5.0)
        v3 = torch.clamp(v2, min=4.0, max=7.0)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 1, 64, 64)
