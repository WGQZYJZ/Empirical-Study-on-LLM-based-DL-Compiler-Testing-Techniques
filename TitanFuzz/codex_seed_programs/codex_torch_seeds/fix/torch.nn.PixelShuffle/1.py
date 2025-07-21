'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.PixelShuffle\ntorch.nn.PixelShuffle(upscale_factor)\n'
import torch
import torch.nn as nn
input_data = torch.randn(1, 4, 4, 4)
print(input_data)
pixel_shuffle = nn.PixelShuffle(2)
output_data = pixel_shuffle(input_data)
print(output_data)