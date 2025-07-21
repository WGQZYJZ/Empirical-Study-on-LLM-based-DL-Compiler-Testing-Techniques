'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_sparse\ntorch.Tensor.is_sparse(_input_tensor, )\n'
import torch
input_tensor = torch.randn(4, 4)
result = torch.Tensor.is_sparse(input_tensor)
print(result)