import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.features = torch.nn.Sequential(torch.nn.Conv2d(1, 30, 3, 1, 0), torch.nn.Conv2d(30, 64, 3, 1, 1), torch.nn.Conv2d(64, 96, 3, 1, 2))
        self.features = torch.nn.Sequential(torch.nn.Conv2d(1, 30, 3, 1, 0), torch.nn.Conv2d(30, 64, 3, 1, 1), torch.nn.Conv2d(64, 96, 3, 1, 2))
        self.features = torch.nn.Sequential(torch.nn.Conv2d(1, 30, 3, 1, 0), torch.nn.Conv2d(30, 64, 3, 1, 1), torch.nn.Conv2d(64, 96, 3, 1, 2))
        self.features = torch.nn.Sequential(torch.nn.Conv2d(1, 30, 3, 1, 0), torch.nn.Conv2d(30, 64, 3, 1, 1), torch.nn.Conv2d(64, 96, 3, 1, 2))
        split = torch.nn.Sequential(torch.nn.Conv2d(96, 64, 3, 1, 1), torch.nn.Conv2d(64, 32, 3, 1, 1))
        self.features = torch.nn.Sequential(torch.nn.Conv2d(1, 30, 3, 1, 0), torch.nn.Conv2d(30, 64, 3, 1, 1), torch.nn.Conv2d(64, 96, 3, 1, 2))
    def forward(self, x1):
        v1 = self.features(x1)
        split_tensors = torch.split(v1, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return (concatenated_tensor, torch.split(v1, [1, 1, 1], dim=1))
m = Model()
# Inputs to the model
x1 = torch.randn(1, 1, 8, 8)
