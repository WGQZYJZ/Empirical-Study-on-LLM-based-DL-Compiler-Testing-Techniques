'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.less\ntorch.Tensor.less(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(4, 4)
other = torch.randn(4, 4)
less_tensor = input_tensor.less(other)
print('input_tensor:', input_tensor)
print('other:', other)
print('less_tensor:', less_tensor)