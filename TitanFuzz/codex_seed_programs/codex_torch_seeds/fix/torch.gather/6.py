'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.gather\ntorch.gather(input, dim, index, *, sparse_grad=False, out=None)\n'
import torch
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('x: ', x)
index = torch.tensor([[1, 1, 1], [1, 1, 1]])
print('index: ', index)
y = torch.gather(x, dim=1, index=index)
print('y: ', y)
print('Expected: ', torch.tensor([[2, 2, 2], [5, 5, 5]]))
print('Actual: ', y)
print('Expected shape: ', torch.Size([2, 3]))
print('Actual shape: ', y.shape)