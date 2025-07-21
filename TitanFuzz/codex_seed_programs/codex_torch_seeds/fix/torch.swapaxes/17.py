'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.swapaxes\ntorch.swapaxes(input, axis0, axis1)\n'
import torch
import torch
input = torch.randn(2, 3, 4)
print('Input size: ', input.size())
output = torch.swapaxes(input, 0, 2)
print('Output size: ', output.size())