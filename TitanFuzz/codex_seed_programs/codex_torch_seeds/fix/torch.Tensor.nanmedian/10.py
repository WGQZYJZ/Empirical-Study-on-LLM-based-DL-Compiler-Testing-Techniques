'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nanmedian\ntorch.Tensor.nanmedian(_input_tensor, dim=None, keepdim=False)\n'
import torch
x = torch.rand(4, 4)
print(x)
print(x.nanmedian())
print(x.nanmedian(dim=0))
print(x.nanmedian(dim=1, keepdim=True))