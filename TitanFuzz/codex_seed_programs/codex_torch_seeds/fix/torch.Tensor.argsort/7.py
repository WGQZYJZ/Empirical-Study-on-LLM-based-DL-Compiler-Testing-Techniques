'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.argsort\ntorch.Tensor.argsort(_input_tensor, dim=-1, descending=False)\n'
import torch
input_tensor = torch.randn(3, 4, 5)
print(input_tensor)
print(input_tensor.argsort(dim=(- 1), descending=False))