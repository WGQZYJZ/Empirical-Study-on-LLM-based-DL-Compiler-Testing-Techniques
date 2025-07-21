'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.broadcast_to\ntorch.Tensor.broadcast_to(_input_tensor, shape)\n'
import torch
_input_tensor = torch.randn(4, 2, 3)
print('Input tensor:', _input_tensor)
_output_tensor = torch.Tensor.broadcast_to(_input_tensor, (4, 2, 3, 4))
print('Output tensor:', _output_tensor)