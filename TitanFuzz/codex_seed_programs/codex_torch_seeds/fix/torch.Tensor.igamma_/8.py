'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.igamma_\ntorch.Tensor.igamma_(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(4, 4)
other_tensor = torch.randn(4, 4)
torch.Tensor.igamma_(input_tensor, other_tensor)
print('input_tensor = ', input_tensor)
print('other_tensor = ', other_tensor)