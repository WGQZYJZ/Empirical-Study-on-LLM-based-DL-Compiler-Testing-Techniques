'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nanmedian\ntorch.Tensor.nanmedian(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
input_tensor[(0, 0, 0)] = float('nan')
input_tensor[(1, 2, 3)] = float('nan')
print(input_tensor)
print(torch.Tensor.nanmedian(input_tensor))
print(torch.Tensor.nanmedian(input_tensor, dim=0))
print(torch.Tensor.nanmedian(input_tensor, dim=1))
print(torch.Tensor.nanmedian(input_tensor, dim=2))
print(torch.Tensor.nanmedian(input_tensor, dim=2, keepdim=True))