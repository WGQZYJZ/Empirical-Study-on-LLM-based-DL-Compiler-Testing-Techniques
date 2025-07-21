'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.std\ntorch.Tensor.std(_input_tensor, dim, unbiased=True, keepdim=False)\n'
import torch
input_tensor = torch.randn(3, 4)
print(input_tensor.std(dim=0, keepdim=True, unbiased=False))
print(input_tensor.std(dim=1, keepdim=True, unbiased=False))