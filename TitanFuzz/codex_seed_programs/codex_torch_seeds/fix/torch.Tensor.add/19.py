'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.add\ntorch.Tensor.add(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.randn(1, 3)
other_tensor = torch.randn(1, 3)
output_tensor = input_tensor.add(other_tensor)
print('input_tensor: ', input_tensor)
print('other_tensor: ', other_tensor)
print('output_tensor: ', output_tensor)