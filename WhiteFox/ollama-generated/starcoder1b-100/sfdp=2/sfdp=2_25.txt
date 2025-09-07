
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(20, 32)
        self.fc2 = torch.nn.Linear(32, 64)
        self.fc3 = torch.nn.Linear(64, 10)

    def forward(self, x):
        x1 = self.fc1(x)
        x2 = self.fc2(x1)
        x3 = F.relu(self.fc3(x2))
        return x3


# Initializing the model
m = Model()
