'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.squeeze\ntorch.Tensor.squeeze(_input_tensor, dim=None)\n'
import torch
import torch
input_tensor = torch.randn(1, 3, 1, 1)
squeeze_tensor = torch.Tensor.squeeze(input_tensor, dim=None)
print('input_tensor:', input_tensor)
print('squeeze_tensor:', squeeze_tensor)