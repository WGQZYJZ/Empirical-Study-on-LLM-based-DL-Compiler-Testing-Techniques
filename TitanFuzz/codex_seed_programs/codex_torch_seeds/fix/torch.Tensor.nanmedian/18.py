'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nanmedian\ntorch.Tensor.nanmedian(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(10, 10)
result = torch.Tensor.nanmedian(input_tensor, dim=1)
print(result)
result = torch.Tensor.nanmedian(input_tensor, dim=1, keepdim=True)
print(result)