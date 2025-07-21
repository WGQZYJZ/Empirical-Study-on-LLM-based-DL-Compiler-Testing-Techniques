import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3, dtype=torch.float32)
output = torch.ones_like(input)