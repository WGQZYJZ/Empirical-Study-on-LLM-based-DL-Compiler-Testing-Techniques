
class Conv1(torch.nn.Module):
    def __init__(self, in_channels: int, out_channels: int, kernel_size: int):
        super().__init__()
        self.conv = torch.nn.Conv2d(in_channels, out_channels, kernel_size)

    def forward(self, x1):
        output  = self.conv(x1)
        return output
class Conv2(torch.nn.Module):
    def __init__(self, in_channels: int, out_channels: int, kernel_size: int):
        super().__init__()
        self.conv = torch.nn.Conv2d(in_channels, out_channels, kernel_size)

    def forward(self, x1):
        output  = self.conv(x1)
        return output
class BatchNorm1D(torch.nn.Module):
    def __init__(self, num_features: int):
        super().__init__()
        self.bn = torch.nn.BatchNorm1d(num_features=num_features)

    def forward(self, x1):
        output  = self.bn(x1)
        return output
class BatchNorm2D(torch.nn.Module):
    def __init__(self, num_features: int):
        super().__init__()
        self.bn = torch.nn.BatchNorm2d(num_features=num_features)

    def forward(self, x1):
        output  = self.bn(x1)
        return output
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        # Convolution layers
        self.conv1 = Conv1(3, 16, kernel_size=5)
        self.conv2 = Conv2(16, 32, kernel_size=4)
        # Batch norm layers
        self.bn1 = BatchNorm1D(num_features=32)
        self.bn2 = BatchNorm2D(num_features=64)

    def forward(self, x1):
        # Forward pass for the convolution layer (module API).
        output  = self.conv1(x1)
        # Forward pass for the batch norm layer (functional API).
        output += F.batch_norm(input=output, num_features=32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=False) 
        output += F.batch_norm(input=output, num_features=64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        return output

# Inputs to the model
x1 = torch.randn(32, 3, 8, 8)
m = Model()
