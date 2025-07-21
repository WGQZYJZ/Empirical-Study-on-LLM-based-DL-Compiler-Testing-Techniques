'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unsqueeze\ntorch.unsqueeze(input, dim)\n'
import torch
input = torch.randn(3, 2)
output = torch.unsqueeze(input, dim=0)
print('Input: {}'.format(input))
print('Output: {}'.format(output))