'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.half\ntorch.Tensor.half(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
import torch
_input_tensor = torch.rand(3, 3)
print('Input tensor: {}'.format(_input_tensor))
_out_tensor = _input_tensor.half()
print('Output tensor: {}'.format(_out_tensor))