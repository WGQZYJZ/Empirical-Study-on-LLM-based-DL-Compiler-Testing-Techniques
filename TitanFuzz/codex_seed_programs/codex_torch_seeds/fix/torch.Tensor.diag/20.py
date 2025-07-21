'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.diag\ntorch.Tensor.diag(_input_tensor, diagonal=0)\n'
import torch
_input_tensor = torch.rand(3, 3)
print(torch.Tensor.diag(_input_tensor, diagonal=0))
print(torch.Tensor.diag(_input_tensor, diagonal=1))
print(torch.Tensor.diag(_input_tensor, diagonal=2))
print(torch.Tensor.diag(_input_tensor, diagonal=3))
print(torch.Tensor.diag(_input_tensor, diagonal=4))
print(torch.Tensor.diag(_input_tensor, diagonal=(- 1)))
print(torch.Tensor.diag(_input_tensor, diagonal=(- 2)))
print(torch.Tensor.diag(_input_tensor, diagonal=(- 3)))
print(torch.Tensor.diag(_input_tensor, diagonal=(- 4)))