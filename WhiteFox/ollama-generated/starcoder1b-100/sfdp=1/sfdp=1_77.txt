
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.bn1  = torch.nn.BatchNorm2d(8)
        self.relu  = torch.nn.ReLU()
        self.conv2 = torch.nn.Conv2d(8, 16, 1)
        self.bn2  = torch.nn.BatchNorm2d(16)
        self.conv3 = torch.nn.Conv2d(16, 32, 1)
        self.bn3  = torch.nn.BatchNorm2d(32)

    def forward(self, x):
        qk = torch.matmul(x, x.transpose(-2, -1)) / math.sqrt(float(math.pi))
        v = self.relu(self.bn1(self.conv1(x)))
        k = self.bn2(self.conv2(v))
        v = self.bn3(self.conv3(k))
        return torch.matmul(v, v.transpose(-2, -1)).tanh()


# Initializing the model
m = Model()

