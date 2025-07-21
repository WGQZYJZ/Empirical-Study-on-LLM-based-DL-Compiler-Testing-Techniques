'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.xlogy\ntorch.Tensor.xlogy(_input_tensor, other)\n'
import torch
input_tensor = torch.rand(10, 10)
other = torch.rand(10, 10)
output_tensor = input_tensor.xlogy(other)
print('input_tensor: ', input_tensor)
print('other: ', other)
print('output_tensor: ', output_tensor)