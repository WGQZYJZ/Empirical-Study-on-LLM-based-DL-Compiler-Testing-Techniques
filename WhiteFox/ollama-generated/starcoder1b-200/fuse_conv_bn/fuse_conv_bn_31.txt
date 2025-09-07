
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 3, 4)
        self.bn1  = torch.nn.BatchNorm2d(3)
        self.relu  = torch.nn.ReLU()
        self.conv2 = torch.nn.Conv2d(3, 5, 4)
        self.bn2  = torch.nn.BatchNorm2d(5)
        self.avg_pool2d = torch.nn.AdaptiveAvgPool2d(1)

    def forward(self, x):
        conv1 = self.conv1(x)
        bn1  = self.bn1(conv1)
        output = self.relu(bn1)
        conv2 = self.conv2(output)
        bn2  = self.bn2(conv2)
        avg_pool2d = self.avg_pool2d(bn2)

        return avg_pool2d


# Initializing the model
m = Model()

