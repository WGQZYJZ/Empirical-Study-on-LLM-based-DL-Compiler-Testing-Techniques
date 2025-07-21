'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.select\ntorch.Tensor.select(_input_tensor, dim, index)\n'
import torch
input_tensor = torch.randn(3, 4)
print('input_tensor:', input_tensor)
result = torch.Tensor.select(input_tensor, dim=0, index=2)
print('result:', result)