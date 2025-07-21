'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clone\ntorch.clone(input, *, memory_format=torch.preserve_format)\n'
import torch
x = torch.rand(10, 1, dtype=torch.float32, requires_grad=True)
y = torch.clone(x)
print('x = ', x)
print('y = ', y)
print('x.data_ptr() = ', x.data_ptr())
print('y.data_ptr() = ', y.data_ptr())
print('x.is_leaf = ', x.is_leaf)
print('y.is_leaf = ', y.is_leaf)
print('x.requires_grad = ', x.requires_grad)
print('y.requires_grad = ', y.requires_grad)