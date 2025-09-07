
class ConvBnModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 10, kernel_size=5)

    def forward(self, x):
        return self.conv(x).relu()


# Initializing the model
mbm  = ConvBnModel()
x1 = torch.randn(10, 3, 480, 640)
