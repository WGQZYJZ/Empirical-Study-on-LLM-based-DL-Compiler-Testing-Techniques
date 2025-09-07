
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v0 = x1  # Copy input tensor to output of the convolution for later use in the pattern matching
        v1  = self.conv(x1)
        v4 = torch.sigmoid(v1)  # Apply sigmoid function to the output of the convolution
        return v4


m  = Model()
x1 = torch.randn(1, 3, 64, 64)
 
