
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3) # Apply convolution to input tensor using kernel size 3
        self.conv2 = torch.nn.Conv2d(3, 16, 4) # Apply convolution to input tensor using kernel size 4
 
    def forward(self, x):
        y = self.conv1(x)  # Convolution of the input tensor with kernel size 3
        y = self.conv2(y)  # Convolution of output of a conv layer with kernel size 4
        return y


# Inputs to the model
x = torch.randn(1, 3, 64, 64)
