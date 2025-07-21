import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.Tensor([[[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]]]))
output = torch.nn.functional.avg_pool2d(input, kernel_size=2, stride=2)