'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.maximum\ntorch.Tensor.maximum(_input_tensor, other)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input_tensor = torch.rand(2, 3)
print('input_tensor: ', input_tensor)
other_tensor = torch.rand(2, 3)
print('other_tensor: ', other_tensor)
print('Task 3: Call the API torch.Tensor.maximum')
result = torch.Tensor.maximum(input_tensor, other_tensor)
print('result: ', result)