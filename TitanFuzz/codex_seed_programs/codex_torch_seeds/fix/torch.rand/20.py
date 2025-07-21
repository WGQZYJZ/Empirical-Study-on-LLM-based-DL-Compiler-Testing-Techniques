'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rand\ntorch.rand(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
print('Task 3: Call the API torch.rand')
print('torch.rand(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)')
print('Generate a tensor with shape (3, 4) and element values are random numbers between [0, 1)')
print(torch.rand(3, 4))
print('Generate a tensor with shape (3, 4) and element values are random numbers between [0, 2)')
print((torch.rand(3, 4) * 2))
print('Generate a tensor with shape (3, 4) and element values are random numbers between [0, 5)')
print((torch.rand(3, 4) * 5))
print('Generate a tensor with shape (3, 4) and element values are random numbers between [0, 10)')
print((torch.rand(3, 4) * 10))