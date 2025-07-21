import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.Tensor([[[[1, 2, 3], [4, 5, 6]]]]))
max_pool_2d = torch.nn.MaxPool2d(kernel_size=2, stride=1)
output = max_pool_2d(input)