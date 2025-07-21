'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.zero_\ntorch.Tensor.zero_(_input_tensor)\n'
import torch
x = torch.randn(2, 3)
y = torch.Tensor.zero_(x)
print(x)
print(y)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fill_\ntorch.Tensor.fill_(_input_tensor, value)\n'
import torch
x = torch.randn(2, 3)
y = torch.Tensor.fill_(x, 2)
print(x)
print(y)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.add_\ntorch.Tensor.add_(_input_tensor, value)\n'
import torch
x = torch.randn(2, 3)
y = torch.Tensor.add_(x, 2)
print