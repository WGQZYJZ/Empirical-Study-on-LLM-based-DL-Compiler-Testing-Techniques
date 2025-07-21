import torch
from torch import nn
from torch.autograd import Variable
input = torch.arange(4, dtype=torch.float32).reshape(2, 2)
repeats = torch.tensor([2, 3])
output = torch.repeat_interleave(input, repeats, dim=0)
output = torch.repeat_interleave(input, repeats, dim=1)