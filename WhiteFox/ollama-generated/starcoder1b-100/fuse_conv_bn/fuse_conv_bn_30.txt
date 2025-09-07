
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(...)  # X can be 1, 3, or 5 representing the dimension
        self.bn   = torch.nn.BatchNorm2d(...)
        self.relu = torch.nn.ReLU()
        self.avgpool2d = torch.nn.AvgPool2d(..., ceil_mode=True)

    def forward(self, x):
        return self.conv(x), self.relu(self.bn(self.avgpool2d(self.conv(x)))))


# Initializing the model
m  = Model()


# Inputs to the model
input_tensor = torch.randn(...) # This should be equal to `output` in the above example, but it cannot.
__output__, __unused_inputs__ = m(*input_tensor)

