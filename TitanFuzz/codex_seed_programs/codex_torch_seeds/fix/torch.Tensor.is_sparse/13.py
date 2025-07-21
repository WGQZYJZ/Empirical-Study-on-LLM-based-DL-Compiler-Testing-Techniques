'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_sparse\ntorch.Tensor.is_sparse(_input_tensor, )\n'
import torch
_input_tensor = torch.randn(1, 3, 4, 4)
print(torch.Tensor.is_sparse(_input_tensor))