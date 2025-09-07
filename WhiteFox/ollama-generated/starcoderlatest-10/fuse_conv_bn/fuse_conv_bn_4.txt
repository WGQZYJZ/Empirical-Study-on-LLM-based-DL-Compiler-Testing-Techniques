
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 16, kernel_size=3)
        self.conv2 = torch.nn.Conv2d(16, 32, kernel_size=3)

    def forward(self, x):
        v1 = torch.nn.functional.conv2d(x, self.conv1.weight, self.conv1.bias, self.conv1.stride, self.conv1.padding, self.conv1.dilation, self.conv1.groups) # apply a convolutional layer (FusedConvolution2d)
        v2 = torch.nn.functional.batch_norm(v1, 0.95, 0.36, self.training, False) # apply batch normalization to the output of FusedConvolution2d
        output = torch.nn.functional.conv2d(v2, self.conv2.weight, self.conv2.bias, self.conv2.stride, self.conv2.padding, self.conv2.dilation, self.conv2.groups) # apply a convolutional layer (FusedConvolution2d)
        return output


# Inputs to the model
x1 = torch.randn(1, 1, 4, 4)
m = Model()
