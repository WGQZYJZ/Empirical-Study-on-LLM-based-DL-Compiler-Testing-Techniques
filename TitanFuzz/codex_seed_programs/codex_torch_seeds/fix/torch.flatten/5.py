'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flatten\ntorch.flatten(input, start_dim=0, end_dim=-1)\n'
import torch
input = torch.randn(1, 3, 4, 5)
print(input.shape)
output = torch.flatten(input)
print(output.shape)
output = torch.flatten(input, start_dim=1)
print(output.shape)
output = torch.flatten(input, start_dim=1, end_dim=2)
print(output.shape)