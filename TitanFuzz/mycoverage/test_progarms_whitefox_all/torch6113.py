import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.features = torch.nn.ModuleList([torch.nn.Conv2d(1, 36, 4, 2, 0), torch.nn.Flatten(), torch.nn.Linear(6048, 4096), torch.nn.Tanh(), torch.nn.Linear(4096, 4)])
    def forward(self, v1):
        split_tensors = torch.split(v1, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return (concatenated_tensor, torch.split(v1, [1, 1, 1], dim=1))
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
