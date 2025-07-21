'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.long\ntorch.Tensor.long(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.randn(2, 3)
print('Input tensor: ', _input_tensor)
_input_tensor = _input_tensor.long()
print('Output tensor: ', _input_tensor)