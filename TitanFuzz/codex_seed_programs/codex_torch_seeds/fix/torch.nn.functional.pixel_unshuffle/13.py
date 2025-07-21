'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pixel_unshuffle\ntorch.nn.functional.pixel_unshuffle(input, downscale_factor)\n'
import torch
import numpy as np
import torch
input = torch.randint(low=0, high=255, size=(1, 1, 4, 4), dtype=torch.uint8)
print(input)
output = torch.nn.functional.pixel_unshuffle(input, 2)
print(output)