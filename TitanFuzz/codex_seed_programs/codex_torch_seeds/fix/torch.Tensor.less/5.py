'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.less\ntorch.Tensor.less(_input_tensor, other)\n'
import torch
import torch
input_tensor = torch.tensor([[1, 2], [3, 4]])
other = torch.tensor([[1, 1], [4, 4]])
output_tensor = input_tensor.less(other)
print('input_tensor:', input_tensor)
print('other:', other)
print('output_tensor:', output_tensor)