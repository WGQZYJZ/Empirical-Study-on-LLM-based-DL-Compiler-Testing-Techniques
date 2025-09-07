
class Model(torch.nn.Module):
    def __init__(self, num_channels: int):
        super().__init__()
        self.conv = torch.nn.Conv2d(num_channels, 8, 3, stride=2, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return v1


# Initializing the model
m = Model(5)

 # Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
