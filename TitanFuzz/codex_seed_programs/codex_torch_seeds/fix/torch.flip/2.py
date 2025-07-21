'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flip\ntorch.flip(input, dims)\n'
import torch
input = torch.randn(3, 5)
print('input: ', input)
flip_input = torch.flip(input, dims=[0])
print('flip_input: ', flip_input)