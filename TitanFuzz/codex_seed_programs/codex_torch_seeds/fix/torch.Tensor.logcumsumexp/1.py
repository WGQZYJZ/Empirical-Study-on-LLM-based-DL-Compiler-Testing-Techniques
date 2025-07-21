'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logcumsumexp\ntorch.Tensor.logcumsumexp(_input_tensor, dim)\n'
import torch
input_tensor = torch.randn(3, 4)
print('Input tensor: \n', input_tensor)
logcumsumexp_tensor = torch.Tensor.logcumsumexp(input_tensor, dim=1)
print('Logcumsumexp tensor: \n', logcumsumexp_tensor)