import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(3, dtype=torch.float32)
output = torch.fix(input)