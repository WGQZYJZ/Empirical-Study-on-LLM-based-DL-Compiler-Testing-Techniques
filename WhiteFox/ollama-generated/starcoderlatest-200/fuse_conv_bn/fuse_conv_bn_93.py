
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, kernel_size=(7, 7), stride=(2, 2)) # ConvX(input tensor, output channels, kernel size (x, y), stride (x, y))
        self.bn = torch.nn.BatchNorm2d(64) # BatchNormX(output tensor of conv layer)

    def forward(self, x):
        return self.bn(F.relu(self.conv1(x)))

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(2, 3, 224, 224) # Batch size is set to 2 for demonstration purposes only. Actual batch size should be greater than or equal to two to get valid results
