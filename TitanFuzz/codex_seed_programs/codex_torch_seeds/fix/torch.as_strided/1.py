'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.as_strided\ntorch.as_strided(input, size, stride, storage_offset=0)\n'
import torch
import numpy as np
input = torch.arange(0, 20)
input = input.view(5, 4)
print('Input is: \n', input)
size = (4, 4)
stride = (4, 1)
output = torch.as_strided(input, size, stride)
print('Output is: \n', output)