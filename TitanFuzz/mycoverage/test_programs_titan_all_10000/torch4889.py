import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.Tensor([[[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]]]))
pool = torch.nn.AvgPool2d(2, stride=2, padding=0)
output = pool(input)