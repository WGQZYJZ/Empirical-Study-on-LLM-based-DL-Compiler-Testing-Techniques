
class Model(torch.nn.Module):
    def __init__(self, out_channels = 2):
        super().__init__()
        self.conv1d = torch.nn.Conv1d(2, out_channels, kernel_size=3)
        self.bn = torch.nn.BatchNormXd(out_channels)

    def forward(self, x1):
        conv1d = self.conv1d(x1)  # Fused convolution and batch normalization will be added here.
        output = self.bn(conv1d)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 200000)
