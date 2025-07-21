'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nanmedian\ntorch.Tensor.nanmedian(_input_tensor, dim=None, keepdim=False)\n'
import torch
_input_tensor = torch.randn(4, 4)
_input_tensor[1][1] = float('nan')
print(_input_tensor)
print(torch.Tensor.nanmedian(_input_tensor, dim=None, keepdim=False))
print(torch.Tensor.nanmedian(_input_tensor, dim=0, keepdim=False))
print(torch.Tensor.nanmedian(_input_tensor, dim=1, keepdim=False))
print(torch.Tensor.nanmedian(_input_tensor, dim=None, keepdim=True))
print(torch.Tensor.nanmedian(_input_tensor, dim=0, keepdim=True))
print(torch.Tensor.nanmedian(_input_tensor, dim=1, keepdim=True))