'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clip\ntorch.Tensor.clip(_input_tensor, min=None, max=None)\n'
import torch
import torch
input_tensor = ((torch.rand(4, 4) * 20) - 10)
torch.Tensor.clip(input_tensor, min=(- 5), max=5)
print(input_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_select\ntorch.Tensor.index_select(_input_tensor, dim, index)\n'
import torch
import torch
input_tensor = torch.rand(4, 4)
torch.Tensor.index_select(input_tensor, 0, torch.tensor([0, 2]))
print(input_tensor)