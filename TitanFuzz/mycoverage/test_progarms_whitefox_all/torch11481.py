import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.features1 = torch.nn.Sequential(*(torch.nn.Conv2d(32, 1, 3, 1, 1) for _ in range(8)))
        self.features2 = torch.nn.Sequential(*(torch.nn.Conv2d(1, 1, 3, 1, 1) for _ in range(6)))
    def forward(self, v1):
        split_tensors = torch.split(v1, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return (concatenated_tensor, torch.split(v1, [1, 1, 1], dim=1))
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64,64)
