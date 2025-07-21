'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.median\ntorch.Tensor.median(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(4, 4)
print(input_tensor.median(dim=0))
print(input_tensor.median(dim=1))
print(input_tensor.median(dim=2))