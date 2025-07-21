'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.trunc\ntorch.Tensor.trunc(_input_tensor)\n'
import torch
_input_tensor = torch.randn(3, 3)
print('input tensor: ', _input_tensor)
_trunc_tensor = _input_tensor.trunc()
print('trunc tensor: ', _trunc_tensor)