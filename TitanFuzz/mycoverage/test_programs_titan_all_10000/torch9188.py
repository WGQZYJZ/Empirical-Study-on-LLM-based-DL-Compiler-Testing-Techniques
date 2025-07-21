import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.Tensor(1, 1, 4, 4, 4).uniform_())
output = torch.nn.functional.max_pool3d(input, kernel_size=3, stride=2, padding=1)