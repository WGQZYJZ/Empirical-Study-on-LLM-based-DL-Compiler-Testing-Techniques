'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nansum\ntorch.Tensor.nansum(_input_tensor, dim=None, keepdim=False, dtype=None)\n'
import torch
_input_tensor = torch.randn(3, 3, requires_grad=True)
print('Input tensor: ', _input_tensor)
_output_tensor = torch.Tensor.nansum(_input_tensor, dim=None, keepdim=False, dtype=None)
print('Output tensor: ', _output_tensor)