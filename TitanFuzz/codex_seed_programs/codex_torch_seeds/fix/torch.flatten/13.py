'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flatten\ntorch.flatten(input, start_dim=0, end_dim=-1)\n'
import torch
import torch
x = torch.tensor([[[1, 1, 1], [1, 1, 1]], [[2, 2, 2], [2, 2, 2]], [[3, 3, 3], [3, 3, 3]]])
x_flatten = torch.flatten(x, start_dim=1, end_dim=(- 1))
print('x_flatten = ', x_flatten)