'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flatten\ntorch.flatten(input, start_dim=0, end_dim=-1)\n'
import torch
x = torch.randint(0, 10, (2, 3, 4))
print(x)
y = torch.flatten(x, start_dim=1, end_dim=(- 1))
print(y)