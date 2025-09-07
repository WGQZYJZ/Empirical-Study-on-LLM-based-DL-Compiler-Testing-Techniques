
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(128, 32)
        self.relu = torch.nn.ReLU()
        self.fc2 = torch.nn.Linear(32, 64)
        self.dropout = torch.nn.Dropout(0.5)
 
    def forward(self, x):
        v1 = torch.cat([x, x], dim=0)
        v2 = self.relu(self.fc1(v1))
        v3 = self.dropout(self.fc2(v2))
        return v3


# Initializing the model
m = Model()

