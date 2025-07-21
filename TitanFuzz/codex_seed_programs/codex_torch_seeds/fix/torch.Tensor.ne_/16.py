'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ne_\ntorch.Tensor.ne_(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[1, 2], [3, 4]])
other = torch.tensor([[1, 2], [3, 4]])
output_tensor = torch.Tensor.ne_(input_tensor, other)
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)