'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clone\ntorch.Tensor.clone(_input_tensor, *, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.rand(2, 3, requires_grad=True)
print('_input_tensor: ', _input_tensor)
_output_tensor = _input_tensor.clone()
print('_output_tensor: ', _output_tensor)
print('_input_tensor is _output_tensor: ', (_input_tensor is _output_tensor))