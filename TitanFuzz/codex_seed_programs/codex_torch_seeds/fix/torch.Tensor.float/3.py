'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.float\ntorch.Tensor.float(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input = torch.rand(2, 3, 4)
print('Input: ', _input)
_input_tensor = torch.Tensor.float(_input)
print('Input Tensor: ', _input_tensor)