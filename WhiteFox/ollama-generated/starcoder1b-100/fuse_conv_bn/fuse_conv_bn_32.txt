
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)
        self.bn = torch.nn.BatchNorm2d(...)
        self.relu = torch.nn.ReLU()

    def forward(self, x1):
        v1 = self.conv(x1)
        bn_out  = self.bn(v1)
        relu_out = self.relu(bn_out)
        return relu_out


# Inputs to the model
inputs = torch.randn(...)
