'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.maximum\ntorch.Tensor.maximum(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(3, 5)
other_tensor = torch.randn(3, 5)
result = torch.Tensor.maximum(input_tensor, other_tensor)
print('input_tensor: ', input_tensor)
print('other_tensor: ', other_tensor)
print('result: ', result)