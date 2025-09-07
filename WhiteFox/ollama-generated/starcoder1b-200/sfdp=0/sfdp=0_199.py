
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3)
        self.bn1   = torch.nn.BatchNorm2d(8)
        self.conv2 = torch.nn.Conv2d(8, 16, 3)
        self.bn2   = torch.nn.BatchNorm2d(16)
        self.fc    = torch.nn.Linear(16 * 7 * 7, 4096)
        self.dropout = torch.nn.Dropout()
        self.fc2   = torch.nn.Linear(4096, 4096)
        self.fc3   = torch.nn.Linear(4096, 1024)
        self.output = torch.nn.Linear(1024, 256)

    def forward(self, x):
        # [batch size] [number of points in batch] [spatial dims (height, width)]
        x = F.relu(self.bn1(self.conv1(x)))
        x = F.max_pool2d(F.relu(self.bn2(self.conv2(x))), 2)
        # Reshape the input tensor into the shape of [batch size * number of points in batch] [spatial dims (height, width)]
        x = x.view(-1, x.size(-2), x.size(-1))
        x = F.relu(self.dropout(self.fc(x)))
        x = self.fc2(x)
        x = F.softmax(self.fc3(x), dim=-1)
        x = x * self.fc2.weight  # Multiply the output by the output of the linear layer before softmax
        # x = torch.exp(self.output(x))
        x = F.log_softmax(self.output(x), dim=-1)
        return x


# Initializing the model
m = Model()


