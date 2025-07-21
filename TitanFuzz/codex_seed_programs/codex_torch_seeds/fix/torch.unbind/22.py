'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unbind\ntorch.unbind(input, dim=0)\n'
import torch
input = torch.randn(2, 3)
print(input)
print(input.shape)
unbind_input = torch.unbind(input, dim=0)
print(unbind_input)
print(len(unbind_input))
print(unbind_input[0].shape)
print(unbind_input[1].shape)