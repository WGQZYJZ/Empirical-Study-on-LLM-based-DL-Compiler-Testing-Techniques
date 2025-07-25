import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 128, 1, stride=1)
        self.conv2 = torch.nn.Conv2d(3, 64, 1, stride=1)
        self.conv3 = torch.nn.Conv2d(64, 8, 1, stride=1)
        self.fc1 = torch.nn.Linear(8, 128)
        self.fc2 = torch.nn.Linear(128, 10)

    def forward(self, x1):
        v1 = torch.relu(self.conv1(x1))
        v2 = torch.relu(self.conv2(x1))
        v3 = torch.relu(self.conv3(v2))
        v4 = v1.flatten(start_dim=1)
        v5 = torch.relu(self.fc1(v4))
        v6 = self.fc2(v5)
        return v6

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
