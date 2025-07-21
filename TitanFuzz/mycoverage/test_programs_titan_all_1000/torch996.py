import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange(1, 101, 1)
output_data = torch.logspace(start=(- 10), end=10, steps=5)