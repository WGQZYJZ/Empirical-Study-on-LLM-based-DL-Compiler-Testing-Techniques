'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.resolve_neg\ntorch.resolve_neg(input)\n'
import torch
input = torch.rand(3, 3)
print('Input:')
print(input)
print('\nOutput:')
print(torch.resolve_neg(input))