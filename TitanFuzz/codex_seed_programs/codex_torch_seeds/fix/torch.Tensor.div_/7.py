'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.div_\ntorch.Tensor.div_(_input_tensor, value, *, rounding_mode=None)\n'
import torch
input_tensor = torch.arange(12, dtype=torch.float32).reshape(3, 4)
print('Input tensor: ', input_tensor)
result_tensor = input_tensor.div_(2)
print('Result tensor: ', result_tensor)