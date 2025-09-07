
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, 7, stride=2, padding=3)
        self.relu1 = torch.nn.ReLU(inplace=True)
        self.maxpool1 = torch.nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv2 = torch.nn.Conv2d(64, 64, 3, stride=1, padding=1)
        self.relu2 = torch.nn.ReLU(inplace=True)
 
    def forward(self, x):
        v1 = self.conv1(x) # Apply pointwise convolution with kernel size 7 to the input tensor and stride of 2 and padding of 3 to get a 48 * 64 * 64 tensor
        v2 = self.relu1(v1) # Apply ReLU on the output of the previous convolution, get a 48 * 64 * 64 tensor
        v3 = self.maxpool1(v2) # Use the pooling layer with kernel size 2 and stride 2 to downsample the input tensor from a 48 * 64 * 64 tensor to a 48 * 32 * 32 tensor, get a 48 * 32 * 32 tensor
        v4 = self.conv2(v3) # Apply pointwise convolution with kernel size 3 and stride 1 and padding of 1 to get an 48 * 64 * 32 tensor
        v5 = self.relu2(v4) # Apply ReLU on the output of the previous convolution, get a 48 * 64 * 32 tensor
        return v5
 
# Initializing the model
m1 = Model()
 
# Inputs to the model
x_input = torch.randn(1, 3, 48, 48) # (bs, channel, height, width)
