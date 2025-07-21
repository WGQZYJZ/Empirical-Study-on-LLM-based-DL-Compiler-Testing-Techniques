'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nanmedian\ntorch.Tensor.nanmedian(_input_tensor, dim=None, keepdim=False)\n'
import torch
x = torch.Tensor([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 1, 1, 1, 1]])
print(x)
print(torch.Tensor.nanmedian(x, dim=0, keepdim=False))
print(torch.Tensor.nanmedian(x, dim=1, keepdim=False))