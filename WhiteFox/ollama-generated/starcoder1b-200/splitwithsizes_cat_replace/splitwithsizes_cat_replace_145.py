
class Model(torch.nn.Module):
    def __init__(self, num_channels: int = 3):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.relu1 = torch.nn.ReLU()
        self.maxpool = torch.nn.MaxPool2d(kernel_size=(2, 2), stride=(2, 2))
        self.conv2 = torch.nn.Conv2d(8, 8, 3)
 
    def forward(self, x1):
        v1 = self.relu1(self.maxpool(self.conv1(x1)))
        v2 = self.maxpool(self.conv2(v1))
        return torch.cat([v1, v2], dim=1)


# Initializing the model
m = Model()

