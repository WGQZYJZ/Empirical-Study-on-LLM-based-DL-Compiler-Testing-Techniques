'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sub_\ntorch.Tensor.sub_(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.randn(2, 3)
other_tensor = torch.randn(2, 3)
torch.Tensor.sub_(input_tensor, other_tensor)
print('input_tensor:', input_tensor)
print('other_tensor:', other_tensor)