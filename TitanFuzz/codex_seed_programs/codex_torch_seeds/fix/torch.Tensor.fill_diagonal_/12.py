'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fill_diagonal_\ntorch.Tensor.fill_diagonal_(_input_tensor, fill_value, wrap=False)\n'
import torch
input_tensor = torch.randn(3, 3)
fill_value = 1
torch.Tensor.fill_diagonal_(input_tensor, fill_value, wrap=False)
print('The input tensor is:\n', input_tensor)