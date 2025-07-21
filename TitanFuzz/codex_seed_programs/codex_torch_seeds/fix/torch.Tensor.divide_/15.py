'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.divide_\ntorch.Tensor.divide_(_input_tensor, value, *, rounding_mode=None)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('Input Tensor:', input_tensor)
value = 2
print('Output Tensor:', input_tensor.divide_(value))