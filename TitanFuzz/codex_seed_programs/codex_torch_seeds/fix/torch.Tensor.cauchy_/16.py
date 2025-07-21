'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cauchy_\ntorch.Tensor.cauchy_(_input_tensor, median=0, sigma=1, *, generator=None)\n'
import torch
_input_tensor = torch.Tensor(2, 3)
print('Input Tensor: ', _input_tensor)
torch.Tensor.cauchy_(_input_tensor, median=0, sigma=1)
print('Output Tensor: ', _input_tensor)