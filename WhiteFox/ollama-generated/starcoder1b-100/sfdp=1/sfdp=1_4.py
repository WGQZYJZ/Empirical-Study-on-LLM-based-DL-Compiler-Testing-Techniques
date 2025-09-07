
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1d = torch.nn.Conv1d(3, 8, 1)
        self.fc1   = torch.nn.Linear(8, 256)
 
    def forward(self, x1):
        v1 = self.conv1d(x1)
        v2 = v1.view(-1, 8, 1).contiguous().flatten()
        v3 = F.relu(self.fc1(v2))
        return v3


# Initializing the model
m = Model()


