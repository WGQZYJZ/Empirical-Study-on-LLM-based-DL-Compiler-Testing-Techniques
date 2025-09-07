
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1)
        self.pool = torch.nn.MaxPool2d(kernel_size=2, stride=2)
        self.fc1 = torch.nn.Linear(16 * 4 * 4, 10)
 
    def forward(self, x1):
        v1 = self.pool(F.relu(self.conv1(x1)))
        v2 = self.pool(F.relu(self.conv2(v1)))
        out = F.log_softmax(self.fc1(torch.cat([v2, v1], dim=1)), dim=1)
        return out


# Initializing the model
m = Model()


