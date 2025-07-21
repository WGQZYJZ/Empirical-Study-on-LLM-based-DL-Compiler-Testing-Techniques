import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[[1, 0, 1], [1, 1, 1], [1, 0, 1]]], dtype=torch.float32)
output = torch.count_nonzero(input)