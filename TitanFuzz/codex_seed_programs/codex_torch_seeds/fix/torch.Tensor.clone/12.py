'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clone\ntorch.Tensor.clone(_input_tensor, *, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.randint(1, 10, (3, 3))
_output_tensor = _input_tensor.clone()
print('Input Tensor: {}'.format(_input_tensor))
print('Output Tensor: {}'.format(_output_tensor))