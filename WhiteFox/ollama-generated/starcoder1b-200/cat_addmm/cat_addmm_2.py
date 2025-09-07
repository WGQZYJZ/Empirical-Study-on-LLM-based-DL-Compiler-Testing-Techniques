
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc1  = torch.nn.Linear(12*64*64, 1024)
        self.fc2  = torch.nn.Linear(1024, 512)
        self.fc3  = torch.nn.Linear(512, 256)
        self.fc4  = torch.nn.Linear(256, 128)
        self.fc5  = torch.nn.Linear(128, 64)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1.view(-1, 12*64*64)
        v3 = F.relu(self.fc1(v2))
        v4 = F.relu(self.fc2(v3))
        v5 = F.relu(self.fc3(v4))
        v6 = self.fc4(v5)
        v7 = self.fc5(v6)
        return torch.sigmoid(v7)


# Initializing the model
m = Model()


