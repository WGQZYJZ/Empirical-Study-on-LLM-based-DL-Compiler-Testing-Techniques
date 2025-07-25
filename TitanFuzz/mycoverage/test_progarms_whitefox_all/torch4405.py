import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.features = torch.nn.ModuleList([torch.nn.Conv2d(3, 32, 7, 2, 3), torch.nn.MaxPool2d(2, 2), torch.nn.Conv2d(32, 64, 3, 2, 1), torch.nn.MaxPool2d(2, 1), torch.nn.Conv2d(64, 128, 3, 1, 1)])
    def forward(self, v1):
        split_tensors = torch.split(v1, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return (concatenated_tensor, torch.split(v1, [1, 1, 1], dim=1))
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
