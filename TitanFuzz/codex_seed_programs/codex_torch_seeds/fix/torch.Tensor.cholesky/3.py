'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cholesky\ntorch.Tensor.cholesky(_input_tensor, upper=False)\n'
import torch
input_tensor = torch.rand(3, 3)
print(input_tensor)
output_tensor = torch.Tensor.cholesky(input_tensor)
print(output_tensor)