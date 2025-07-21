'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.div\ntorch.Tensor.div(_input_tensor, value, *, rounding_mode=None)\n'
import torch
input_tensor = torch.randn(1, 3)
print('Input Tensor: ', input_tensor)
div_tensor = torch.Tensor.div(input_tensor, 2)
print('Div Tensor: ', div_tensor)