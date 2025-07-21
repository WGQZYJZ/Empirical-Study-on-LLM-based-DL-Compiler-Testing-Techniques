'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unsqueeze\ntorch.unsqueeze(input, dim)\n'
import torch
x = torch.tensor([1, 2, 3, 4])
print('x: ', x)
y = torch.unsqueeze(x, 0)
print('y: ', y)
z = torch.unsqueeze(x, 1)
print('z: ', z)