
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        return v1 + other


# Initializing the model and passing additional tensor as a keyword argument to convolution operation
m  = Model()
x1 = torch.randn(2048, 3, 64, 64)
v1 = m(x1)  # Output of convolutional layer with input size (2048, 3, 64, 64), 8 feature maps per output channel and kernel size 1.
other  = torch.randn(25, 17, 19, 18) # Size (25, 17, 19, 18). Any valid PyTorch tensor.
__output__  = m(x1, other=other)

