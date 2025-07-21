'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_floating_point\ntorch.Tensor.is_floating_point(_input_tensor)\n'
import torch
_input_tensor = torch.rand(3, 3)
_result = _input_tensor.is_floating_point()
print('_input_tensor: {}'.format(_input_tensor))
print('_result: {}'.format(_result))