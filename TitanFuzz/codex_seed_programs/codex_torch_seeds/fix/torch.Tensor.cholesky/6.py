'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cholesky\ntorch.Tensor.cholesky(_input_tensor, upper=False)\n'
import torch
input_tensor = torch.randn(2, 2)
print('Input Tensor: ', input_tensor)
cholesky_tensor = torch.Tensor.cholesky(input_tensor)
print('Cholesky Tensor: ', cholesky_tensor)