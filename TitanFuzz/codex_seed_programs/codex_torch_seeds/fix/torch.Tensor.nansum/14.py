'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nansum\ntorch.Tensor.nansum(_input_tensor, dim=None, keepdim=False, dtype=None)\n'
import torch
_input_tensor = torch.randn(4, 4)
print(_input_tensor)
print(torch.Tensor.nansum(_input_tensor, dim=None, keepdim=False, dtype=None))
print(torch.Tensor.nansum(_input_tensor, dim=0, keepdim=False, dtype=None))
print(torch.Tensor.nansum(_input_tensor, dim=1, keepdim=False, dtype=None))
_input_tensor = torch.randn(4, 4)
_input_tensor[1][1] = float('nan')
print(_input_tensor)
print(torch.Tensor.nansum(_input_tensor, dim=None, keepdim=False, dtype=None))