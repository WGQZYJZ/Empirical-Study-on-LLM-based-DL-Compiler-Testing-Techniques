'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mode\ntorch.mode(input, dim=-1, keepdim=False, *, out=None)\n'
import torch
import torch
input_data = torch.tensor([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 1, 1, 1, 1]])
output_data = torch.mode(input_data, dim=0, keepdim=False)
print('output_data:', output_data)