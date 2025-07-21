'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cpu\ntorch.Tensor.cpu(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
import torch
_input_tensor = torch.rand(2, 3, 4, 5, 6)
_out_tensor = _input_tensor.cpu(memory_format=torch.preserve_format)
print('Input tensor: {}'.format(_input_tensor))
print('Output tensor: {}'.format(_out_tensor))