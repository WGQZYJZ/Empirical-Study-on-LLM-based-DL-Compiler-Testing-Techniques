
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(...)  # ConvXd is equivalent to functional.conv2d
        self.batch_norm1 = torch.nn.BatchNorm2d(...)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.batch_norm1(v1)
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
