'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unsqueeze\ntorch.unsqueeze(input, dim)\n'
import torch
x = torch.tensor([1, 2, 3, 4])
print('x: ', x)
y = torch.unsqueeze(x, dim=0)
print('y: ', y)
y = torch.unsqueeze(x, dim=1)
print('y: ', y)