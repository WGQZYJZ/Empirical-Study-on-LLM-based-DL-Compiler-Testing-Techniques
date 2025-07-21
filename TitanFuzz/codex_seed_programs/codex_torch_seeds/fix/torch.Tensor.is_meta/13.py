'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_meta\ntorch.Tensor.is_meta(_input_tensor, )\n'
import torch
x = torch.randn(2, 3)
out = torch.Tensor.is_meta(x)
print(out)