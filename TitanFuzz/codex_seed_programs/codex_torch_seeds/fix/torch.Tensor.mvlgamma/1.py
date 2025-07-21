'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mvlgamma\ntorch.Tensor.mvlgamma(_input_tensor, p)\n'
import torch
_input_tensor = torch.randn(3, 3)
print('Input Tensor: ', _input_tensor)
print('Output: ', torch.Tensor.mvlgamma(_input_tensor, 3))