'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.argsort\ntorch.Tensor.argsort(_input_tensor, dim=-1, descending=False)\n'
import torch
x = torch.randn(1, 5)
print(x)
print(x.argsort(dim=(- 1), descending=True))