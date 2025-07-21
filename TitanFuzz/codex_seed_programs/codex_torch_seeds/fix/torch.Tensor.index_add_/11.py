'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_add_\ntorch.Tensor.index_add_(_input_tensor, dim, index, tensor, *, alpha=1)\n'
import torch
input_tensor = torch.randn(3, 4)
print(input_tensor)
torch.Tensor.index_add_(input_tensor, 1, torch.tensor([0, 1, 2, 3]), torch.tensor([1, 2, 3, 4]))
print(input_tensor)
torch.Tensor.index_add_(input_tensor, 1, torch.tensor([0, 1, 2, 3]), torch.tensor([1, 2, 3, 4]), alpha=0.5)
print(input_tensor)