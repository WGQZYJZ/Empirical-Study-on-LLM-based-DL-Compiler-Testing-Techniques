'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.half\ntorch.Tensor.half(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.randn(4, 4, dtype=torch.float32)
print('Input tensor: ', _input_tensor)
_half_tensor = torch.Tensor.half(_input_tensor, memory_format=torch.preserve_format)
print('Half tensor: ', _half_tensor)
_half_tensor = torch.Tensor.half(_input_tensor, memory_format=torch.channels_last)
print('Half tensor: ', _half_tensor)