'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_zeros\ntorch.Tensor.new_zeros(_input_tensor, size, dtype=None, device=None, requires_grad=False)\n'
import torch
_input_tensor = torch.rand(3, 3)
_output_tensor = torch.Tensor.new_zeros(_input_tensor, size=(3, 3), dtype=None, device=None, requires_grad=False)
print('Output tensor: ', _output_tensor)