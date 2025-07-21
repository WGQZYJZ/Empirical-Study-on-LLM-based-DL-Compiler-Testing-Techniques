'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cholesky_inverse\ntorch.Tensor.cholesky_inverse(_input_tensor, upper=False)\n'
import torch
input_tensor = torch.rand(3, 3)
torch.Tensor.cholesky_inverse(input_tensor, upper=False)