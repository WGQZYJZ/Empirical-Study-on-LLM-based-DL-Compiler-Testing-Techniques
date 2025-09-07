
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(256, 1024)
        self.fc2 = torch.nn.Linear(1024, 512)
        self.fc3 = torch.nn.Linear(512, 8)
 
    def forward(self, x):
        v = F.relu(self.fc1(x))
        v = F.relu(self.fc2(v))
        v = self.fc3(v)
        return v


# Initializing the model
m = Model()

