import torch
from torch import nn

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(2, 3),
            nn.ReLU(),
            nn.Tanh(),
            nn.Tanh()
        )
    def forward(self, x):
        x = self.layers(x)
        return x
m = Model()
# Inputs to the model
x = torch.randn(2, 2)
