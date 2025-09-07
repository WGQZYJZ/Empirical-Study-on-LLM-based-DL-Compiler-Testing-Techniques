
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, 7, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(64, 64, 1, stride=1, padding=0)
        self.fc1 = torch.nn.Linear(512 * 3 * 3, 256)
        self.fc2 = torch.nn.Linear(256, 10)
 
    def forward(self, x1):
        v1  = self.conv1(x1).view(-1, 512, 3, 3)
        v2  = torch.relu(self.conv2(v1))
        v3  = torch.flatten(v2, 1)
        v4  = torch.relu(self.fc1(v3))
        return self.fc2(v4)


# Initializing the model
m  = Model()


