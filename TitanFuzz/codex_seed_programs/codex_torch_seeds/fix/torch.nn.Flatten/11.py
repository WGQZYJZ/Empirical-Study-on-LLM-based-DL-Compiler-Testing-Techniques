'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Flatten\ntorch.nn.Flatten(start_dim=1, end_dim=-1)\n'
import torch
import torch.nn as nn
in_data = torch.randn(1, 3, 32, 32)
print(in_data.shape)
flatten = nn.Flatten()
out_data = flatten(in_data)
print(out_data.shape)