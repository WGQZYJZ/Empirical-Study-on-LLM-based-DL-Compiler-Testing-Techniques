import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3, 4, 4)
pixel_unshuffle = torch.nn.PixelUnshuffle(2)
output = pixel_unshuffle(input)