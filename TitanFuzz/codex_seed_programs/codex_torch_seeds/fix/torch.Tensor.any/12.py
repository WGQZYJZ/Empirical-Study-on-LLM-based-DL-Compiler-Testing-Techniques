'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.any\ntorch.Tensor.any(_input_tensor, dim=None, keepdim=False)\n'
import torch
_input_tensor = torch.randn(2, 3)
print('Input tensor:\n', _input_tensor)
_any = torch.Tensor.any(_input_tensor)
print('Any of the elements in the input tensor is non-zero?\n', _any)
_any = torch.Tensor.any(_input_tensor, dim=0)
print('Any of the elements in the input tensor is non-zero in the 0-th dimension?\n', _any)
_any = torch.Tensor.any(_input_tensor, dim=1)
print('Any of the elements in the input tensor is non-zero in the 1-st dimension?\n', _any)
_any = torch.Tensor.any(_input_tensor, dim=1, keepdim=True)
print('Any of the elements in the input tensor is non-zero in the 1-st dimension?\n', _any)