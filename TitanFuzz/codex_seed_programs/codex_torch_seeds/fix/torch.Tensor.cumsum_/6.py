'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cumsum_\ntorch.Tensor.cumsum_(_input_tensor, dim, dtype=None)\n'
import torch
input_tensor = torch.randn(3, 4)
print('Input Tensor: ', input_tensor)
result = input_tensor.cumsum_(dim=1)
print('Result: ', result)