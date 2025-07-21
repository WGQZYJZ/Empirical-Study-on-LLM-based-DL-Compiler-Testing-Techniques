'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.char\ntorch.Tensor.char(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.randn(1, 3, 5, 5)
_input_tensor_char = _input_tensor.char()
print('_input_tensor_char = ', _input_tensor_char)
'\nTask 4: Call the API torch.Tensor.byte\ntorch.Tensor.byte(_input_tensor, memory_format=torch.preserve_format)\n'
_input_tensor_byte = _input_tensor.byte()
print('_input_tensor_byte = ', _input_tensor_byte)
'\nTask 5: Call the API torch.Tensor.short\ntorch.Tensor.short(_input_tensor, memory_format=torch.preserve_format)\n'
_input_tensor_short = _input_tensor.short()
print('_input_tensor_short = ', _input_tensor_short)