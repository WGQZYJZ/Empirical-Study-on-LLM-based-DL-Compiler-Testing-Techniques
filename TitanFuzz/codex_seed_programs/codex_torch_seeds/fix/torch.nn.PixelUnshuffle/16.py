'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.PixelUnshuffle\ntorch.nn.PixelUnshuffle(downscale_factor)\n'
import torch
from torch.nn import PixelUnshuffle
input = torch.randn(1, 1, 4, 4)
pixel_unshuffle = PixelUnshuffle(downscale_factor=2)
output = pixel_unshuffle(input)
print('Input: ', input)
print('Output: ', output)