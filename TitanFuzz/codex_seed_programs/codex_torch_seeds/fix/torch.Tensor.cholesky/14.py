'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cholesky\ntorch.Tensor.cholesky(_input_tensor, upper=False)\n'
import torch
input_tensor = torch.randn(3, 3)
cholesky_result = torch.Tensor.cholesky(input_tensor, upper=False)
print('cholesky_result: ', cholesky_result)