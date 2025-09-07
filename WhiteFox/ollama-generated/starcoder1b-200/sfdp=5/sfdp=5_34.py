
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1) # Apply 1-dimensional convolution to input tensor 0.
        self.conv2 = torch.nn.Conv2d(8, 16, 1) # Apply 1-dimensional convolution to input tensor 1.
 
    def forward(self, x):
        h1 = self.conv1(x)  # Compute the 1-dimensional convolution from input tensor 0 to output tensor 1.
        h2 = self.conv2(h1)  # Compute the 1-dimensional convolution from output tensor 1 to output tensor 2.
        return h2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)  # Input 0
y1 = torch.randn(1, 8, 64, 64)  # Input 1
