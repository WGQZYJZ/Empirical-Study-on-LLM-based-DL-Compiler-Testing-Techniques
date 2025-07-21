import torch
from torch import nn
from torch.autograd import Variable
input = torch.arange(1, 5, dtype=torch.float32).reshape(1, 1, 2, 2)
pad = [1, 1, 1, 1]
mode = 'constant'
value = 0.0
output = torch.nn.functional.pad(input, pad, mode=mode, value=value)