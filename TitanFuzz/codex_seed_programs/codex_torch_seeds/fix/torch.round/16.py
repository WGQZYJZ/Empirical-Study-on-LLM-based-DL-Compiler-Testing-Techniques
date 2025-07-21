'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.round\ntorch.round(input, *, out=None)\n'
import torch
x = torch.tensor(1.3)
y = torch.tensor(1.7)
round_x = torch.round(x)
round_y = torch.round(y)
print(round_x)
print(round_y)