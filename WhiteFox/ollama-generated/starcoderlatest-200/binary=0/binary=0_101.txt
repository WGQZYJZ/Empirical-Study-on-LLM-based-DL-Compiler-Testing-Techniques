
class Model(torch.nn.Module):
    def __init__(self, conv_input: int, conv_kernel: int, conv_stride: int, other: torch.tensor = None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other
        return v6


# Initializing the model
m = Model(8, 5, 4, torch.ones([1, conv_input, 32, 32]))


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
