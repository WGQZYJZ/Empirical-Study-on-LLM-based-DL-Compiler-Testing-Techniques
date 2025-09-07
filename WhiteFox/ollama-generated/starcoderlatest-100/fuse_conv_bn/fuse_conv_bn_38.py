
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(...)  # input_channels, kernel_size, stride=1 and padding=0

    def forward(self, x1):
        x1 = self.conv1(x1)
        return x1


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.bn  = torch.nn.BatchNorm2d(...) # n_features, momentum=0.1, eps=1e-5

    def forward(self, x1):
        x1 = self.conv1(x1)
        return bn(x1)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.bn  = torch.nn.BatchNorm2d(...) # n_features=3, momentum=0.1, eps=1e-5

    def forward(self, x1):
        x1 = nn.functional.conv2d(...) 
        return bn(x1)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.bn  = torch.nn.BatchNorm2d(...) # n_features=3, momentum=0.1

    def forward(self, x1):
        x1 = nn.functional.conv2d(x1, ...) 
        return bn(x1)


# Input to the model
x1 = torch.randn(1, 3, 48, 64)
