'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.PixelUnshuffle\ntorch.nn.PixelUnshuffle(downscale_factor)\n'
import torch
from torch.autograd import Variable
dtype = torch.FloatTensor
input = Variable(torch.randn(1, 1, 4, 4).type(dtype), requires_grad=False)
pixel_unshuffle = torch.nn.PixelUnshuffle(2)
output = pixel_unshuffle(input)
print('input: ', input)
print('output: ', output)