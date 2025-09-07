
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 + 3).clamp(min=0)  # Add 3 to the output of the convolution
        v3 = v2.clamp(max=6)  # Clamp the output of the addition operation to a minimum of 0 and a maximum of 6
        v4 = v3 / 6  # Divide the output of the previous operation by 6
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
