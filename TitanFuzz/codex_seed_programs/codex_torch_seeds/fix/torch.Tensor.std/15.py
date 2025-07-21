'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.std\ntorch.Tensor.std(_input_tensor, dim, unbiased=True, keepdim=False)\n'
import torch
_input_tensor = torch.rand(3, 3)
print('Input Tensor:\n', _input_tensor)
_std_tensor = _input_tensor.std(dim=0, unbiased=True, keepdim=False)
print('Standard deviation Tensor:\n', _std_tensor)