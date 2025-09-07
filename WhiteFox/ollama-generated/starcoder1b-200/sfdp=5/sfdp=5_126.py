
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 4, 1, stride=1, padding=0)
        self.fc1   = torch.nn.Linear(5760, 1024)
        self.fc2   = torch.nn.Linear(1024, 2)
 
    def forward(self, x1):
        v1  = self.conv1(x1)
        v2  = self.conv2(v1)
        v3  = v2.flatten(1)
        v4  = v3.view(-1, 5760)
        v5  = torch.relu(self.fc1(v4))
        v6  = self.fc2(v5)
        return v6


# Initializing the model
m = Model()

