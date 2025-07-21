'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.PixelUnshuffle\ntorch.nn.PixelUnshuffle(downscale_factor)\n'
import torch
from torch.autograd import Variable
from torch.nn import PixelUnshuffle
input_data = torch.randn(1, 1, 4, 4)
input_data = Variable(input_data)
pixel_unshuffle = PixelUnshuffle(2)
output_data = pixel_unshuffle(input_data)
print(output_data)