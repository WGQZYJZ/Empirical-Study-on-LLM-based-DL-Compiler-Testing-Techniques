'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Flatten\ntorch.nn.Flatten(start_dim=1, end_dim=-1)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input_data = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(input_data.shape)
flatten = nn.Flatten(start_dim=1, end_dim=(- 1))
output = flatten(input_data)
print(output.shape)
print(output)