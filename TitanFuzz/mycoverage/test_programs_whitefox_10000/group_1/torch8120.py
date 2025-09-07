import torch
from torch import nn

class Model(nn.Module):
  def __init__(self):
    super().__init__()
    self.m = torch.nn.Linear(1,1)
# Inputs to the model
x = torch.randn(1,1,1)
