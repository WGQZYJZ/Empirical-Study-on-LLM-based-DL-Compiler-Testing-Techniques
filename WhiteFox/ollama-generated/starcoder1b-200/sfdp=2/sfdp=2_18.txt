
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(64, 8)
        self.fc2 = torch.nn.Linear(8, 8)
        self.fc3 = torch.nn.Linear(8, 2)

    def forward(self, x):
        v0 = self.fc1(x).view(-1, 512)
        v1 = F.relu(self.fc2(v0))
        v2 = F.relu(self.fc3(v1))
        return F.log_softmax(v2)


# Initializing the model
m = Model()

