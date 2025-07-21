import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
topk_output = torch.topk(input, 2)