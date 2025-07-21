'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cummin\ntorch.Tensor.cummin(_input_tensor, dim)\n'
import torch
input_tensor = torch.randn(10, 3)
print(input_tensor)
print('cummin(input_tensor, dim=0)')
print(torch.Tensor.cummin(input_tensor, dim=0))
print('cummin(input_tensor, dim=1)')
print(torch.Tensor.cummin(input_tensor, dim=1))
print('cummin(input_tensor, dim=2)')
print(torch.Tensor.cummin(input_tensor, dim=2))