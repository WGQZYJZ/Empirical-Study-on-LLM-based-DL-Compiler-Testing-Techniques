'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Flatten\ntorch.nn.Flatten(start_dim=1, end_dim=-1)\n'
import torch
data = torch.randn(2, 3, 5)
print(data)
flatten = torch.nn.Flatten(start_dim=1, end_dim=(- 1))
print(flatten(data))