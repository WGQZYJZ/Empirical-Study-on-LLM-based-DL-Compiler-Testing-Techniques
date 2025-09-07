
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.bn1 = torch.nn.BatchNorm2d(8)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
        self.bn2 = torch.nn.BatchNorm2d(8)

    def forward(self, x):
        output = self.bn1(self.conv1(x))
        output = self.bn2(self.conv2(output))
        return output


# Initializing the model
m = Model()


