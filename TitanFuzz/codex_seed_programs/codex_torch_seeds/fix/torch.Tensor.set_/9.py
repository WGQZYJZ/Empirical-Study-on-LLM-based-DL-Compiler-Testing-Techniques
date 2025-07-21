'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.set_\ntorch.Tensor.set_(_input_tensor, source=None, storage_offset=0, size=None, stride=None)\n'
import torch
_input_tensor = torch.rand(2, 3)
print('Input tensor: ', _input_tensor)
_input_tensor.set_(torch.rand(2, 3))
print('Output tensor: ', _input_tensor)