import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 5)
k = 2
(value, index) = torch.topk(input, k)