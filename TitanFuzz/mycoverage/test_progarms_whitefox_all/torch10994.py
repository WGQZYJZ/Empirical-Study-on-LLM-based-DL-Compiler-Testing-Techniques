import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.features = torch.nn.ModuleDict({'block0': torch.nn.Conv2d(3, 32, 3, 1, 1, bias=False), 'block1': torch.nn.Sequential(torch.nn.Conv2d(32, 32, 3, 1, 1, bias=False), torch.nn.Conv2d(32, 32, 3, 1, 1, bias=False))})
    def forward(self, v1):
        split_tensors = torch.split(v1, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return (concatenated_tensor, torch.split(v1, [1, 1, 1], dim=1))
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
