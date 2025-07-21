'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_tensor\ntorch.Tensor.new_tensor(_input_tensor, data, dtype=None, device=None, requires_grad=False)\n'
import torch
_input_tensor = torch.randn(4, 3)
_output_tensor = torch.Tensor.new_tensor(_input_tensor, data=_input_tensor, dtype=None, device=None, requires_grad=False)
print('_input_tensor: ', _input_tensor)
print('_output_tensor: ', _output_tensor)