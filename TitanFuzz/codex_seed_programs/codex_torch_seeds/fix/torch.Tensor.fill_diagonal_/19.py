'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fill_diagonal_\ntorch.Tensor.fill_diagonal_(_input_tensor, fill_value, wrap=False)\n'
import torch
input_tensor = torch.randn(3, 3)
print(input_tensor)
input_tensor.fill_diagonal_(0)
print(input_tensor)
input_tensor.fill_diagonal_(1)
print(input_tensor)
input_tensor.fill_diagonal_(2)
print(input_tensor)
input_tensor.fill_diagonal_(3, wrap=True)
print(input_tensor)