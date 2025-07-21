'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flatten\ntorch.flatten(input, start_dim=0, end_dim=-1)\n'
import torch
input = torch.randn(1, 2, 3, 4)
print('Input shape: ', input.shape)
output = torch.flatten(input)
print('Output shape: ', output.shape)