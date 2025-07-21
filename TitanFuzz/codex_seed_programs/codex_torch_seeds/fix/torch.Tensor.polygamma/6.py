'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.polygamma\ntorch.Tensor.polygamma(_input_tensor, n)\n'
import torch
input_tensor = torch.rand(3, 3)
print('Input Tensor: ', input_tensor)
result = input_tensor.polygamma(8)
print('Result: ', result)