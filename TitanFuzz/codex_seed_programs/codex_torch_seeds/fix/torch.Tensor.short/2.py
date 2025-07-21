'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.short\ntorch.Tensor.short(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.randn(2, 3, 5, 5)
_output_tensor = torch.Tensor.short(_input_tensor, memory_format=torch.preserve_format)
print('Input Tensor: ', _input_tensor)
print('Output Tensor: ', _output_tensor)