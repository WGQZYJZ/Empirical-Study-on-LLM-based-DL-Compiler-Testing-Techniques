'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.vdot\ntorch.Tensor.vdot(_input_tensor, other)\n'
import torch
_input_tensor = torch.arange(1, 7, dtype=torch.float32).view(2, 3)
print('Input tensor: ', _input_tensor)
result = _input_tensor.vdot(_input_tensor)
print('Result: ', result)