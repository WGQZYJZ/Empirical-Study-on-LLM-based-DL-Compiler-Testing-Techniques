'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.PixelUnshuffle\ntorch.nn.PixelUnshuffle(downscale_factor)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(1, 3, 4, 4))
print('input data: ', input_data)
unshuffle = torch.nn.PixelUnshuffle(2)
output = unshuffle(input_data)
print('output: ', output)