
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1) # Apply pointwise convolution with kernel size 1 to the input tensor
        self.bn = torch.nn.BatchNorm2d(8) # Batch normalization layer for stabilization
        self.conv2 = torch.nn.Conv2d(8, 16, 3) # Apply pointwise convolution with kernel size 3 to the output of the previous operation

    def forward(self, x1):
        v1 = self.conv1(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2 = self.bn(v1) # Batch normalization layer for stabilization
        v3 = torch.relu(v2) # Apply a rectified linear unit (ReLU) function to the output of the previous operation
 
        v4 = self.conv2(v3) # Apply pointwise convolution with kernel size 3 to the output of the previous operation

        return v4
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
