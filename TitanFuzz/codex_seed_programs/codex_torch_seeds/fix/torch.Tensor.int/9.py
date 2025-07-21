'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.int\ntorch.Tensor.int(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.randn(2, 3, 4, 5)
_input_tensor_int = torch.Tensor.int(_input_tensor)
print('_input_tensor: ', _input_tensor)
print('_input_tensor_int: ', _input_tensor_int)
'\nTask 4: Call the API torch.Tensor.long\ntorch.Tensor.long(_input_tensor, memory_format=torch.preserve_format)\n'
_input_tensor_long = torch.Tensor.long(_input_tensor)
print('_input_tensor_long: ', _input_tensor_long)
'\nTask 5: Call the API torch.Tensor.short\ntorch.Tensor.short(_input_tensor, memory_format=torch.preserve_format)\n'
_input_tensor_short = torch.Tensor.short(_input_tensor)
print('_input_tensor_short: ', _input_tensor_short)