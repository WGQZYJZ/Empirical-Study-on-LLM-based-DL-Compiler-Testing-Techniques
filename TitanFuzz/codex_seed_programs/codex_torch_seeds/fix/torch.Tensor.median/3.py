'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.median\ntorch.Tensor.median(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(2, 3)
print(input_tensor)
print(input_tensor.median(dim=1))
print(input_tensor.median(dim=1, keepdim=True))
print(input_tensor.median(dim=0))
print(input_tensor.median(dim=0, keepdim=True))