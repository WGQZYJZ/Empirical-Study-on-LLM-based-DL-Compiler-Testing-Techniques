import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv1d(3, 3, 3)
        self.bn = torch.nn.BatchNorm1d(3)
    def forward(self, x1):
        x1 = self.bn(x1)
        x1 = F.log_softmax(x1, dim=1)
        return x1
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 4)
