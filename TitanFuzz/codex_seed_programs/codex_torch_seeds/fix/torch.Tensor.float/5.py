'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.float\ntorch.Tensor.float(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.ones([2, 2])
print('Input tensor: ', _input_tensor)
output_tensor = torch.Tensor.float(_input_tensor, memory_format=torch.preserve_format)
print('Output tensor: ', output_tensor)