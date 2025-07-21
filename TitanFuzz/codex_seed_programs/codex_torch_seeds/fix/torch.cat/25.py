'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cat\ntorch.cat(tensors, dim=0, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
y = torch.tensor([[7, 8, 9], [10, 11, 12]])
print('x: \n{}\ny: \n{}'.format(x, y))
print('Task 3: Call the API torch.cat')
z = torch.cat((x, y), dim=0)
print('z: \n{}'.format(z))
z = torch.cat((x, y), dim=1)
print('z: \n{}'.format(z))