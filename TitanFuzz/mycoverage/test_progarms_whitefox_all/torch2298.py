import torch
from torch import nn

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(2, 2)
        self.fc2 = nn.Linear(2, 2)
    def forward(self, x):
        x = self.layers(x)
        x = self.fc2(x)
        x = torch.stack(([x, x]), dim=1) 
        return x
m = Model()
# Inputs to the model
x = torch.randn(2, 2)
