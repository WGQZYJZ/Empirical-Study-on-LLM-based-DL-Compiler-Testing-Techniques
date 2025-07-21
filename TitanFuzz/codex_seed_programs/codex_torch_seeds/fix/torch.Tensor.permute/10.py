'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.permute\ntorch.Tensor.permute(_input_tensor, *dims)\n'
import torch
_input_tensor = torch.randn(2, 3, 4)
print('Input tensor:')
print(_input_tensor)
_output_tensor = _input_tensor.permute(1, 0, 2)
print('Output tensor:')
print(_output_tensor)