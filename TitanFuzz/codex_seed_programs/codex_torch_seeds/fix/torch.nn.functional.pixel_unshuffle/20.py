'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pixel_unshuffle\ntorch.nn.functional.pixel_unshuffle(input, downscale_factor)\n'
import torch
import torch.nn.functional as F
input_data = torch.rand(4, 3, 4, 4)
output = F.pixel_unshuffle(input_data, 2)
print(output)
print(output.shape)