import torch
from torch import nn
from torch.autograd import Variable
dtype = torch.FloatTensor
input = Variable(torch.randn(1, 1, 4, 4).type(dtype), requires_grad=False)
pixel_unshuffle = torch.nn.PixelUnshuffle(2)
output = pixel_unshuffle(input)