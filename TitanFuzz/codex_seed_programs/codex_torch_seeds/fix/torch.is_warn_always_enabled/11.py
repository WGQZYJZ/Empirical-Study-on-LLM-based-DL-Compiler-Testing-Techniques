'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_warn_always_enabled\ntorch.is_warn_always_enabled()\n'
import torch
x = torch.Tensor([[1, 2], [3, 4]])
y = torch.Tensor([[5, 6], [7, 8]])
z = torch.Tensor([[9, 10], [11, 12]])
print(torch.is_warn_always_enabled())