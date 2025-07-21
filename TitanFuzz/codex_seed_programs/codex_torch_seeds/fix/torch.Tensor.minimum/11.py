'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.minimum\ntorch.Tensor.minimum(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(2, 3)
other = torch.randn(3)
result = input_tensor.minimum(other)
print('input_tensor: ', input_tensor)
print('other: ', other)
print('result: ', result)