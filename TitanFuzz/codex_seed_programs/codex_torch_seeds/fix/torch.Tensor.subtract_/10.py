'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.subtract_\ntorch.Tensor.subtract_(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.rand(3, 2)
print('Input tensor: ', input_tensor)
result = torch.Tensor.subtract_(input_tensor, other=0.5)
print('Result: ', result)
print('\n')
result = torch.Tensor.subtract_(input_tensor, other=0.5, alpha=0.5)
print('Result: ', result)