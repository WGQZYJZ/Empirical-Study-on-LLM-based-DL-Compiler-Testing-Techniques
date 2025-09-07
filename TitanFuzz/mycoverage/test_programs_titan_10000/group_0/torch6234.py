import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(1, 3, 5, 5, dtype=torch.float32)
output = torch.empty_like(input)