'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_zero_point\ntorch.Tensor.q_zero_point(_input_tensor)\n'
import torch
_input_tensor = torch.randn(3, 3)
print('Input tensor: ', _input_tensor)
_zero_point = _input_tensor.q_zero_point()
print('Zero point: ', _zero_point)