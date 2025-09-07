
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=0)
        self.fc   = torch.nn.Linear(4 * 4 * 8, 3)
    
    def forward(self, x1):
        v1 = F.relu(self.conv1(x1))
        v2 = F.relu(self.conv2(v1))
        v3 = v2.view(-1, 4 * 4 * 8)
        v4 = self.fc(v3)
        return v4


# Initializing the model
m = Model()

