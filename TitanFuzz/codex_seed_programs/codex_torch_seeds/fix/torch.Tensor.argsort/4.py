'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.argsort\ntorch.Tensor.argsort(_input_tensor, dim=-1, descending=False)\n'
import torch
input_tensor = torch.rand(2, 3)
print(input_tensor)
print(torch.Tensor.argsort(input_tensor, dim=(- 1), descending=False))
print(torch.Tensor.argsort(input_tensor, dim=0, descending=False))
print(torch.Tensor.argsort(input_tensor, dim=1, descending=False))
print(torch.Tensor.argsort(input_tensor, dim=(- 1), descending=True))
print(torch.Tensor.argsort(input_tensor, dim=0, descending=True))
print(torch.Tensor.argsort(input_tensor, dim=1, descending=True))