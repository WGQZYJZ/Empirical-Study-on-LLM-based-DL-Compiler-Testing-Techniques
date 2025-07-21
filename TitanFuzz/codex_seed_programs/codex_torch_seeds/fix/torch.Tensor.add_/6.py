'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.add_\ntorch.Tensor.add_(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.randn(2, 3)
other_tensor = torch.randn(2, 3)
input_tensor.add_(other_tensor)
print('input_tensor after add_: ', input_tensor)
input_tensor.add_(other_tensor, alpha=2)
print('input_tensor after add_: ', input_tensor)