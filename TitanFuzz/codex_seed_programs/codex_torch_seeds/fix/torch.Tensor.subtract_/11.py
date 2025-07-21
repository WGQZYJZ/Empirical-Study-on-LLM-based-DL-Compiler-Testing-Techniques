'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.subtract_\ntorch.Tensor.subtract_(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.randn(5, 3)
other = torch.randn(5, 3)
result = torch.Tensor.subtract_(input_tensor, other)
print('input_tensor: ', input_tensor)
print('other: ', other)
print('result: ', result)