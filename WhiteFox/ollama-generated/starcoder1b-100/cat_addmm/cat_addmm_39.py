
class Model(torch.nn.Module):
    def __init__(self, num_features: int = 32, kernel_size: int = 5, stride: int = 1):
        super().__init__()
        self.conv = torch.nn.Conv2d(in_channels=3, out_channels=num_features, kernel_size=kernel_size,
                                     stride=stride, padding=(kernel_size - 1) // 2)
 
    def forward(self, x):
        v = self.conv(x)
        return v


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
