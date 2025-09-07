
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = F.relu(self.conv(x1)) # Apply rectified linear activation function to the output of the convolution
        v2 = self.conv(v1) # Apply pointwise convolution with kernel size 1 to the output of the rectified linear activation function
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
