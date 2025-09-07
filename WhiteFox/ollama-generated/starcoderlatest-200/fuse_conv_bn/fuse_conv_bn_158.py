
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(...)
        self.bn = torch.nn.BatchNorm2d(...)
        self.linear  = torch.nn.Linear(...)

    def forward(self, x):
        output_conv = self.conv1(x) # ConvXd
        output_bn = self.bn(output_conv) # BatchNormXd
        output_linear = torch.nn.functional.linear(output_bn, ...)
        return output_linear

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 20, 20)
