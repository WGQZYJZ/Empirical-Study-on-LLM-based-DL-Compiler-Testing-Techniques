'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.diag\ntorch.Tensor.diag(_input_tensor, diagonal=0)\n'
import torch
x = torch.rand(3, 3)
print(x)
print(x.diag())
print(x.diag(diagonal=1))
print(x.diag(diagonal=(- 1)))