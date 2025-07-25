import torch
from torch import nn

class Model(torch.nn.Module):
  def __init__(self):
      super().__init__()
      block = [torch.nn.Conv2d(3, 32, 3, 1 - 1 + 1, 0 - 0 + 1, bias=False)]
      self.features = torch.nn.Sequential(*block * 10)
      self.linear = torch.nn.Linear(10, 3)
  def forward(self, v1):
      split_tensors = torch.split(v1, [1, 1, 1], dim=1)
      concatenated_tensor = torch.cat(split_tensors, dim=1)
      return (concatenated_tensor, torch.split(v1, [1, 1, 1], dim=1))
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
