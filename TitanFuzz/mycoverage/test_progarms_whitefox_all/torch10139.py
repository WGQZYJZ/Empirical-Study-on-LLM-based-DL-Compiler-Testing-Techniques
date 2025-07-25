import torch
from torch import nn

class Block(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.features = torch.nn.Sequential(*[torch.nn.Conv2d(3, 8, 3, 1, 1, bias=False)])
    def forward(self, v1):
        split_tensors = torch.split(v1, [2, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return concatenated_tensor
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        model = Block()
        self.features = torch.nn.Sequential(model)
    def forward(self, v1):
        split_tensors = torch.split(v1, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return split_tensors
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
