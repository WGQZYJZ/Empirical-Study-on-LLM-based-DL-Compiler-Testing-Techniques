 2
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 3, 4)
        self.bn    = torch.nn.BatchNorm2d(16, affine=True)

    def forward(self, x1):
        x2  = x1.permute(...) # Permute the input tensor
        x2  = torch.nn.functional.conv2d(x2, ...) # Apply convolutional transformation to the permuted tensor
        x3  = self.bn(x2)           # Apply batch normalization transformation on output of ConvXd
        return x3

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 1, 64, 64)
