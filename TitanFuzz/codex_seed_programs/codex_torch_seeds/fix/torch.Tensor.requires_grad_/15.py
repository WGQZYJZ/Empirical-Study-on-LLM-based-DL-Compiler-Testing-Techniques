'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.requires_grad_\ntorch.Tensor.requires_grad_(_input_tensor, requires_grad=True)\n'
import torch
input_data = torch.randn(10, 3)
print('Input data: \n', input_data)
input_data.requires_grad_(True)
print('Input data: \n', input_data)