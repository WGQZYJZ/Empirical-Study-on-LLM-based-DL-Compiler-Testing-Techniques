'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.angle\ntorch.angle(input, *, out=None)\n'
import torch
input = torch.randn(3, 3)
print('Input: \n', input)
output = torch.angle(input)
print('Output: \n', output)