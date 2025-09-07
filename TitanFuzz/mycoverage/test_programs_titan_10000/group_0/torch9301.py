import torch
from torch import nn
from torch.autograd import Variable

input = torch.empty(5, 3)
output = torch.zeros_like(input)