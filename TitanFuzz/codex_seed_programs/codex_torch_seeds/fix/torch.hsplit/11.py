'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hsplit\ntorch.hsplit(input, indices_or_sections)\n'
import torch
import torch
input = torch.randn(8, 6)
print('Input: \n', input)
output = torch.hsplit(input, 3)
print('Output: \n', output)