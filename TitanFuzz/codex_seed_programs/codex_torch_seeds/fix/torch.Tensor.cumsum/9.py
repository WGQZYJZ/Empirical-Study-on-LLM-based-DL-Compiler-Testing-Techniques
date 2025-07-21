'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cumsum\ntorch.Tensor.cumsum(_input_tensor, dim, dtype=None)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input tensor: \n', input_tensor)
print('Sum along axis 0: \n', input_tensor.cumsum(0))
print('Sum along axis 1: \n', input_tensor.cumsum(1))