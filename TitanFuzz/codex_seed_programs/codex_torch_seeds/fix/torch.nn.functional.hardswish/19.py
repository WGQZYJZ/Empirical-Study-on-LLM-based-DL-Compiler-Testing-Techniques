'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardswish\ntorch.nn.functional.hardswish(input, inplace=False)\n'
import torch
import numpy as np
import torch
input = torch.rand(2, 3, 4)
output = torch.nn.functional.hardswish(input)
print('input:', input)
print('output:', output)