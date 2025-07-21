'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cholesky\ntorch.Tensor.cholesky(_input_tensor, upper=False)\n'
import torch
import torch
input_tensor = torch.randn(4, 4)
result_tensor = torch.Tensor.cholesky(input_tensor, upper=False)
print(input_tensor)
print(result_tensor)