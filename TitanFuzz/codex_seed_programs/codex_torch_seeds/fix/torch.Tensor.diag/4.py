'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.diag\ntorch.Tensor.diag(_input_tensor, diagonal=0)\n'
import torch
input_tensor = torch.randn(3, 3)
print(input_tensor)
print(input_tensor.diag(diagonal=0))
print(input_tensor.diag(diagonal=1))
print(input_tensor.diag(diagonal=(- 1)))