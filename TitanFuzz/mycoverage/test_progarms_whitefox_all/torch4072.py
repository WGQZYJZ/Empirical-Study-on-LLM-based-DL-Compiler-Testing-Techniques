import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 3, (1, 1), stride=(1, 1))
        self.linear = torch.nn.Linear(3, 4)
        self.relu = torch.nn.ReLU()
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = self.linear(v1)
        v3 = self.relu(v2)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 1, 1)
