
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 2, kernel_size=2, stride=2)
        self.bn1 = torch.nn.BatchNorm2d(2)

    def forward(self, x):
        conv_output = self.conv1(x) # use input tensor instead of ConvXd module to test the optimization
        bn_output  = self.bn1(conv_output) # use output tensor instead of BatchNormXd module
        return bn_output

# Inputs to the model
x1 = torch.randn(2, 2, 200, 400)
