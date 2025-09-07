
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, 5, stride=2)
        self.bn1 = torch.nn.BatchNorm2d(64)
        self.conv2 = torch.nn.Conv2d(64, 64, 3, stride=2)
        self.bn2 = torch.nn.BatchNorm2d(64)
        self.pool = torch.nn.MaxPool2d(kernel_size=2, stride=2)
 
    def forward(self, x1):
        t1 = self.conv1(x1)  # Apply a convolution with kernel size 5 to the input tensor
        t2 = self.bn1(t1)  # Batch normalization using running statistics on a single channel
        t3 = torch.tanh(t2)  # Hyperbolic tangent function applied to the output of the previous operation
        t4 = self.pool(t3)  # Max pooling with a window size of 2 and stride 2 to the output of the hyperbolic tangent function
        t5 = self.conv2(t4)  # Apply another convolution with kernel size 3 to the output of the previous operation
        t6 = self.bn2(t5)  # Batch normalization using running statistics on a single channel
        t7 = torch.tanh(t6)  # Hyperbolic tangent function applied to the output of the previous operation
        t8 = self.pool(t7)  # Max pooling with a window size of 2 and stride 2 to the output of the hyperbolic tangent function
        