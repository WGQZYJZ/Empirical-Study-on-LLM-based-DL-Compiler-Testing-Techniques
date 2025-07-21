'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.igamma_\ntorch.Tensor.igamma_(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(4, 4)
other = torch.randn(4, 4)
out = torch.Tensor.igamma_(input_tensor, other)
print('input_tensor: ', input_tensor)
print('out: ', out)