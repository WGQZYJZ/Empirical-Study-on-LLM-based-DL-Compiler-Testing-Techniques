'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.PixelUnshuffle\ntorch.nn.PixelUnshuffle(downscale_factor)\n'
import torch
input = torch.randn(1, 1, 4, 4)
output = torch.nn.PixelUnshuffle(2)(input)
print(input)
print(output)