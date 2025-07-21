'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.movedim\ntorch.movedim(input, source, destination)\n'
import torch
input = torch.randn(2, 3, 4)
print('Input: ', input)
print('Input shape: ', input.shape)
output = torch.movedim(input, 0, 1)
print('Output: ', output)
print('Output shape: ', output.shape)