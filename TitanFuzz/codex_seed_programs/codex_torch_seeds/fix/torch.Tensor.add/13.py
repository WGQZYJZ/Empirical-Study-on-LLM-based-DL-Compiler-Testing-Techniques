'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.add\ntorch.Tensor.add(_input_tensor, other, *, alpha=1)\n'
import torch
_input_tensor = torch.randn(3, 3)
_output_tensor = _input_tensor.add(1)
print('Input tensor: ', _input_tensor)
print('Output tensor: ', _output_tensor)