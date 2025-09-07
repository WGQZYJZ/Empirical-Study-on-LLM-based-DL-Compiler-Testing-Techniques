
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(in_channels=3, out_channels=30, kernel_size=(4,), stride=(1,))  # ConvXd
        self.bn = torch.nn.BatchNorm2d(num_features=30)

    def forward(self, x):
        conv_output = F.conv2d(input=x, weight=self.conv1.weight, bias=self.conv1.bias, stride=self.conv1.stride)
        bn_output = self.bn(conv_output)
        return bn_output

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 40, 20) # x is a tensor with more than 4 dimensions and it's shape can be dynamic
