'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.div_\ntorch.Tensor.div_(_input_tensor, value, *, rounding_mode=None)\n'
import torch
input_tensor = torch.rand(3, 3)
print('input_tensor: ', input_tensor)
print('result: ', input_tensor.div_(2))
print('result: ', input_tensor.div_(2, out=torch.empty(3, 3)))
print('result: ', input_tensor.div_(2, out=torch.empty(3, 3).fill_(3)))