
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) - other # Subtract 'other' from the output of the convolution
        return v1

# Initializing the model
m = Model(torch.randn(2, 3, 64, 64))


# Inputs to the model
x1 = torch.randn(2, 3, 64, 64) # Input to the first layer of the network
