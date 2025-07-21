'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hardshrink\ntorch.Tensor.hardshrink(_input_tensor, lambd=0.5)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
print('Input tensor: ', input_tensor)
print('torch.Tensor.hardshrink(input_tensor, lambd=0.5)')
print(torch.Tensor.hardshrink(input_tensor, lambd=0.5))
print('torch.Tensor.hardshrink(input_tensor, lambd=1)')
print(torch.Tensor.hardshrink(input_tensor, lambd=1))
print('torch.Tensor.hardshrink(input_tensor, lambd=2)')
print(torch.Tensor.hardshrink(input_tensor, lambd=2))