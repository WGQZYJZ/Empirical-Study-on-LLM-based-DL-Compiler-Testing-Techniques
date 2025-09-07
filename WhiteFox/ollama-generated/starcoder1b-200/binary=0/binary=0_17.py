
class Model(torch.nn.Module):
    def __init__(self, x2):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + x2 # Add the value of "x2" to the output of the convolution
        return v1

# Initializing the model
m = Model(torch.randn(1, 3, 64, 64))


