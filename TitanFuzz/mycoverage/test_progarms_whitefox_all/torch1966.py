import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.features = torch.nn.Sequential(torch.nn.Conv2d(3, 3, 3, 1, 1), torch.nn.Conv2d(3, 3, 3, 1, 1))
        self._modules['features']._modules['1'].stride = (2, 3)
        self.split = torch.nn.Sequential(torch.nn.MaxPool2d(3, 2, 1, 0))
    def forward(self, v1):
        split_tensors = torch.split(v1, [1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return (concatenated_tensor, torch.split(v1, [1], dim=1))
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
