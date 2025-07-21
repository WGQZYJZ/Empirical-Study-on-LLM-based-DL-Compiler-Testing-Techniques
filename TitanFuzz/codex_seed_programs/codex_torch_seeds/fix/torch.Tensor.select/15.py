'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.select\ntorch.Tensor.select(_input_tensor, dim, index)\n'
import torch
a = torch.randn(4, 4)
print('a: ', a)
print('torch.Tensor.select(a, 1, 2): ', torch.Tensor.select(a, 1, 2))