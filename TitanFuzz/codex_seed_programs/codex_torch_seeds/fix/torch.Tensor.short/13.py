'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.short\ntorch.Tensor.short(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.rand(2, 3, 4, 5)
_output_tensor = _input_tensor.short()
print('Input tensor: ', _input_tensor)
print('Output tensor: ', _output_tensor)