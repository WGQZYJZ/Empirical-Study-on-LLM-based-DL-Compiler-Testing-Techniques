'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cumsum\ntorch.Tensor.cumsum(_input_tensor, dim, dtype=None)\n'
import torch
input_tensor = torch.randn(3, 4)
print('input_tensor: {}'.format(input_tensor))
print('torch.Tensor.cumsum(input_tensor, dim=0): {}'.format(torch.Tensor.cumsum(input_tensor, dim=0)))
print('torch.Tensor.cumsum(input_tensor, dim=1): {}'.format(torch.Tensor.cumsum(input_tensor, dim=1)))