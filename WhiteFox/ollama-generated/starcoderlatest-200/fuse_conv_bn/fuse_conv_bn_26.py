
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(2, 3, 2)
        self.bn1 = torch.nn.BatchNorm2d(3)
        self.conv2 = torch.nn.Conv2d(3, 3, 2)
        self.bn2 = torch.nn.BatchNorm2d(3)

    def forward(self, x):
        conv_out1 = F.relu(self.bn1(self.conv1(x)))
        conv_out2 = F.relu(self.bn2(self.conv2(conv_out1)))

        return conv_out2


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(2, 2, 4, 4)
