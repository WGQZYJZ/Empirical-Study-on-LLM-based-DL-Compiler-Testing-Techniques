'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pixel_unshuffle\ntorch.nn.functional.pixel_unshuffle(input, downscale_factor)\n'
import torch
from torch.autograd import Variable
import torch
input = torch.rand(1, 3, 4, 4)
output = torch.nn.functional.pixel_unshuffle(input, 2)
print(output)