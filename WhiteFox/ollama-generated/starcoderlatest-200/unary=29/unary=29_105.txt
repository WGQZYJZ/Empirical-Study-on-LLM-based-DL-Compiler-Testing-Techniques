
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.ConvTranspose2d(in_channels=8, out_channels=4, kernel_size=16, stride=16, output_padding=0, bias=True, dilation=1)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.clamp(v1, min=-1, max=1)
        v3 = torch.clamp(v2, min=10, max=25)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
