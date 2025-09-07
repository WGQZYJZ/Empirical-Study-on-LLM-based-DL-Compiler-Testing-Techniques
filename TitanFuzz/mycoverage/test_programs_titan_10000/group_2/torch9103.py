import torch
from torch import nn
from torch.autograd import Variable

input = torch.arange(1, 4, dtype=torch.float32)
repeats = 3
output = torch.repeat_interleave(input, repeats, dim=0)