import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.features1 = torch.nn.Sequential(torch.nn.ReLU6(), torch.nn.MaxPool2d(kernel_size=3, stride=1, padding=1), torch.nn.ReLU6(), torch.nn.MaxPool2d(kernel_size=3, stride=1, padding=1), torch.nn.ReLU6(), torch.nn.MaxPool2d(kernel_size=3, stride=1, padding=1))
    def forward(self, v1):
        split_tensors = torch.split(v1, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return concatenated_tensor
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
