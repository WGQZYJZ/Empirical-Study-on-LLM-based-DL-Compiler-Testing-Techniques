'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.divide_\ntorch.Tensor.divide_(_input_tensor, value, *, rounding_mode=None)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float)
print('Input Tensor: ', input_tensor)
divided_tensor = torch.Tensor.divide_(input_tensor, 2)
print('Divided Tensor: ', divided_tensor)