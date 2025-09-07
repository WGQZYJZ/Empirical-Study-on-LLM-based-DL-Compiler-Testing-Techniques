
class Model(torch.nn.Module):
    def __init__(self, conv_num_features=2048, bn_momentum=0.1):
        super().__init__()

        self.conv1 = torch.nn.Conv2d(1, conv_num_features // 2, kernel_size=5, stride=3)
        self.bn1 = torch.nn.BatchNorm2d(conv_num_features // 2, momentum=bn_momentum)
        self.pool = torch.nn.MaxPool2d(kernel_size=4)

        self.conv2 = torch.nn.Conv2d(conv_num_features // 2, conv_num_features // 4, kernel_size=5, stride=3)
        self.bn2 = torch.nn.BatchNorm2d(conv_num_features // 4, momentum=bn_momentum)

        self.conv3 = torch.nn.Conv2d(conv_num_features // 4, conv_num_features, kernel_size=3, stride=1)
        self.bn3 = torch.nn.BatchNorm2d(conv_num_features, momentum=bn_momentum)

        self.fc = torch.nn.Linear(conv_num_features, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = self.pool(F.relu(self.bn1(x)))
        x = self.conv2(x)
        x = F.relu(self.bn2(x))
        x = self.conv3(x)
        return self.fc(self.bn3(x)).flatten(1)


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(4, 1, 28, 28)
