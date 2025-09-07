import torch
from torch import nn
from torch.autograd import Variable

input = Variable(torch.Tensor(1, 1, 3, 3))
upsample = torch.nn.Upsample(scale_factor=2, mode='nearest')
output = upsample(input)