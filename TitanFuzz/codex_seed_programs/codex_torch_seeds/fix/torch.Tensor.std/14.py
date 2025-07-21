'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.std\ntorch.Tensor.std(_input_tensor, dim, unbiased=True, keepdim=False)\n'
import torch
a = torch.rand(2, 3)
print(a)
print(a.std())
print(a.std(dim=0))
print(a.std(dim=1))
print(a.std(dim=1, unbiased=False))
print(a.std(dim=1, keepdim=True))