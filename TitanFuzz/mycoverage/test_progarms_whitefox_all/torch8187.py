import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.features = torch.nn.ModuleList([torch.nn.BatchNorm2d(4)])
        self.features2 = torch.nn.ModuleList([torch.nn.Conv2d(4, 4, 1, 1, 0, bias=True)])
    def forward(self, v1):
        split_tensors = torch.split(v1, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return (concatenated_tensor, torch.split(v1, [1, 1, 1], dim=1))
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
