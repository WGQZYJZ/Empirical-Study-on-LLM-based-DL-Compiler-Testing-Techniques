'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nelement\ntorch.Tensor.nelement(_input_tensor)\n'
import torch
_input_tensor = torch.rand(2, 3)
print('input tensor:', _input_tensor)
_output = _input_tensor.nelement()
print('output:', _output)