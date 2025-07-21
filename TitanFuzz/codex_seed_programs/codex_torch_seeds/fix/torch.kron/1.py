'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.kron\ntorch.kron(input, other, *, out=None)\n'
import torch
print('PyTorch version: ')
print(torch.__version__)
print('Configuration: ')
print(torch.__config__.show())
print('Is compiled with CUDA: ')
print(torch.cuda.is_available())
input = torch.randn(2, 3)
other = torch.randn(4, 5)
print('\nInput: ')
print(input)
print('Other: ')
print(other)
print('Result: ')
print(torch.kron(input, other))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.kthvalue\ntorch.kthvalue(input, k, dim=None, keepdim=False, *, out=None)\n'
import torch
print('PyTorch version: ')
print