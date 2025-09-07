import torch
from torch import nn
from torch.autograd import Variable

input = torch.empty(3, 3)
output = torch.full_like(input, fill_value=10)