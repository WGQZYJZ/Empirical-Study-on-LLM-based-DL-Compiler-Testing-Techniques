'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.squeeze_\ntorch.Tensor.squeeze_(_input_tensor, dim=None)\n'
import torch
input_tensor = torch.randn(1, 2, 1, 3)
print('input_tensor: ', input_tensor)
squeeze_tensor = torch.Tensor.squeeze_(input_tensor, dim=2)
print('squeeze_tensor: ', squeeze_tensor)
squeeze_tensor = torch.Tensor.squeeze_(input_tensor)
print('squeeze_tensor: ', squeeze_tensor)