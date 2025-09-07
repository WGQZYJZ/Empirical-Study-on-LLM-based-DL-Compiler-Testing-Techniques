
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + other # Add another tensor to the output of the convolution
        v2 = torch.relu(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
other = 0.5 * (torch.ones_like(x1) + x1 / 64.) # A tensor of random values
x1 = torch.randn(1, 3, 28, 28)
 
