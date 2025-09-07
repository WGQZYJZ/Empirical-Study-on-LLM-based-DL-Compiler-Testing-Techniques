
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvXd(3, 256, kernel_size=7)
        self.conv2 = torch.nn.ConvXd(256, 2048, kernel_size=1)
        self.bn1 = torch.nn.BatchNormXd(2048)

    def forward(self, x):
        return self.bn1(torch.nn.functional.convXd(x, self.conv1))

# Initializing the model