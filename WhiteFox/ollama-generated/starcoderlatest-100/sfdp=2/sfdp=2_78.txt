
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(8, 4, 3, stride=2)
        self.conv2 = torch.nn.Conv2d(4, 8, 1, stride=2)
 
    def forward(self, x):
        # The input tensor is first downsampled by a stride of 2 to reduce the spatial dimension by one unit in all dimensions
        x_1 = self.conv1(x)
        # Next we have two convolutional layers that have filters with kernel sizes 3 and 1, respectively. As in the case above, they are used as pointwise layers
        # Convolution layer 1 reduces the input tensor to 4 channels
        x_2 = self.conv2(x_1)
        # The output tensor is then upsampled by a stride of 2 from the input tensor downsampled by two times in all dimensions. Note that there is no ReLU in this case, which may affect the performance
        return x_2


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 8, 32, 32)
