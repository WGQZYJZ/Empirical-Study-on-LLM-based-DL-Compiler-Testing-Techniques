'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flip\ntorch.flip(input, dims)\n'
import torch
inp = torch.randn(1, 2, 3, 4)
print('Input tensor: ', inp)
print('\nFlip tensor along dim=1: ', torch.flip(inp, dims=[1]))
print('\nFlip tensor along dim=2: ', torch.flip(inp, dims=[2]))
print('\nFlip tensor along dim=3: ', torch.flip(inp, dims=[3]))
print('\nFlip tensor along dim=1 and dim=3: ', torch.flip(inp, dims=[1, 3]))
print('\nFlip tensor along dim=1, dim=2 and dim=3: ', torch.flip(inp, dims=[1, 2, 3]))
print('\nFlip tensor along dim=0, dim=1, dim=2 and dim=3: ', torch.flip(inp, dims=[0, 1, 2, 3]))