 
class ConvModule(torch.nn.Module):
    def __init__(self, num_channels: int) -> None:
        super().__init__()
        self.conv = torch.nn.ConvXd(num_input_channels=1, num_output_channels=num_channels, kernel_size=(1, 2))

    def forward(self, x):
        output = x + self.conv(x)
        return output

class BatchModule(torch.nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.bn = torch.nn.BatchNormXd()

    def forward(self, x):
        output = self.bn(x) + self.conv(x)
        return output

class Model(torch.nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.num_features  = 10
        self.conv          = ConvModule(self.num_features)
        self.batch         = BatchModule()

    def forward(self, x):
        output = self.conv(x) + self.batch(x)
        return output
# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2, 1)
