'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_empty\ntorch.Tensor.new_empty(_input_tensor, size, dtype=None, device=None, requires_grad=False)\n'
import torch
_input = torch.randn(2, 2)
print('Input tensor: ', _input)
_output = torch.Tensor.new_empty(_input, (2, 2))
print('Output tensor: ', _output)