'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gt_\ntorch.Tensor.gt_(_input_tensor, other)\n'
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
output_tensor = torch.Tensor.gt_(input_tensor, 3)
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)