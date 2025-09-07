
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(in_channels=1, out_channels=64, kernel_size=(3, 3), stride=(1, 1), padding=(0, 0), dilation=(1, 1))
        self.bn = torch.nn.BatchNorm2d(num_features=64)

    def forward(self, x):
        output = self.conv(x)
        return self.bn(output)


# Initializing the model
m = Model()

