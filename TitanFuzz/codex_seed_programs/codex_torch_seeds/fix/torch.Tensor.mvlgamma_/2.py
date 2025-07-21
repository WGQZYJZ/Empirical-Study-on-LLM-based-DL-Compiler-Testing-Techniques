'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mvlgamma_\ntorch.Tensor.mvlgamma_(_input_tensor, p)\n'
import torch
_input_tensor = torch.rand(3, 3)
print('Input Tensor: ', _input_tensor)
print('Output Tensor: ', torch.Tensor.mvlgamma_(_input_tensor, 3))