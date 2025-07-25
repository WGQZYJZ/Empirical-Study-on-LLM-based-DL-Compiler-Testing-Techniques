import torch
from torch import nn

class Model1(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.features = torch.nn.ModuleList([torch.nn.Conv2d(3, 16, 3, 1, 1)])
    def forward(self, v1):
        split_tensors = torch.split(v1, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return concatenated_tensor
m = Model()
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.branch1 = Model1()
        self.branch2 = Model1()
        self.other_features = torch.nn.Sequential(torch.nn.ReLU(inplace=True))
    def forward(self, v1):
        split_tensors = torch.split(v1, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return (concatenated_tensor, torch.split(v1, [1, 1, 1], dim=1))
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
