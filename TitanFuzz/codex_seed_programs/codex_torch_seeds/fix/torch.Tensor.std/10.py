'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.std\ntorch.Tensor.std(_input_tensor, dim, unbiased=True, keepdim=False)\n'
import torch
import torch
input_tensor = torch.randn(3, 3)
print(input_tensor.std(dim=0))
print(input_tensor.std(dim=1))
print(input_tensor.std(dim=0, unbiased=False))
print(input_tensor.std(dim=1, keepdim=True))