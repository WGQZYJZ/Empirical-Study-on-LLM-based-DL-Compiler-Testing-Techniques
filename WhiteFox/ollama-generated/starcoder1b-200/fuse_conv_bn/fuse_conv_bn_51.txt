
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(...)
        self.bn    = torch.nn.BatchNorm2d(...)

    def forward(self, input_tensor):
        output_tensor = self.conv(input_tensor)
        # If necessary, add the operation to track running statistics, which is not required when fusing convolution and batch normalization layers together, but this example demonstrates how it can be done.
        bn = self.bn(output_tensor)
        return bn


# Inputs to the model
x1  = torch.randn(1, 2, 5, 5)
