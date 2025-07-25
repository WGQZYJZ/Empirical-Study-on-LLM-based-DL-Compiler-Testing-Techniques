import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.features = torch.nn.Sequential(torch.nn.Conv2d(3, 32, 1, 1, 0), torch.nn.BatchNorm2d(32), torch.nn.ReLU(inplace=False), torch.nn.MaxPool2d(2, 2, 0))
    def forward(self, v1):
        split_tensors = torch.split(v1, (1, 1, 1), dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return (concatenated_tensor, torch.split(v1, (1, 1, 1), dim=1))
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
