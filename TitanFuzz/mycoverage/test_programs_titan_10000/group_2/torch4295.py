import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.arange(12)
output = torch.repeat_interleave(input_data, repeats=3, dim=0)