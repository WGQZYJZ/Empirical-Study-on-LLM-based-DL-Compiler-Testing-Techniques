'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.div_\ntorch.Tensor.div_(_input_tensor, value, *, rounding_mode=None)\n'
import torch
input_tensor = torch.rand(5, 3, dtype=torch.float64)
print('Input tensor: ', input_tensor)
div_result = input_tensor.div_(2)
print('Div result: ', div_result)