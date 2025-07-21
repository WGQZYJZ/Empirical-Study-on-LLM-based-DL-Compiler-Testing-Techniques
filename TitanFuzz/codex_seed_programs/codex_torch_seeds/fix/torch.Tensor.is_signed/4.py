'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_signed\ntorch.Tensor.is_signed(_input_tensor)\n'
import torch
_input_tensor = torch.randn((3, 3))
_is_signed = torch.Tensor.is_signed(_input_tensor)
print('Is the input tensor signed: ', _is_signed)