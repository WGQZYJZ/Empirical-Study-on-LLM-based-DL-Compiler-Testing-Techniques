import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.Tensor([[[1, 2, 3, 4, 5, 6, 7]]]))
maxpool = torch.nn.AdaptiveMaxPool1d(3)
output = maxpool(input)