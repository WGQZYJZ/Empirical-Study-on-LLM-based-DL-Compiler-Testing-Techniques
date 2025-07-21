'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.subtract_\ntorch.Tensor.subtract_(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
other = torch.tensor([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
print('Input tensor: ', input_tensor)
print('Other tensor: ', other)
print('Subtracting other from input tensor: ', torch.Tensor.subtract_(input_tensor, other))
print('Subtracting input tensor from other: ', torch.Tensor.subtract_(other, input_tensor))
print('Subtracting input tensor from other with alpha=2: ', torch.Tensor.subtract_(other, input_tensor, alpha=2))