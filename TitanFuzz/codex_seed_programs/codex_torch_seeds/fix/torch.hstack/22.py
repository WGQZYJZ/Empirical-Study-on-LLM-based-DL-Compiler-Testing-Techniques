'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hstack\ntorch.hstack(tensors, *, out=None)\n'
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
y = torch.tensor([[7, 8, 9], [10, 11, 12]])
z = torch.hstack((x, y))
print('Input:')
print('x:', x)
print('y:', y)
print('Output:')
print('z:', z)