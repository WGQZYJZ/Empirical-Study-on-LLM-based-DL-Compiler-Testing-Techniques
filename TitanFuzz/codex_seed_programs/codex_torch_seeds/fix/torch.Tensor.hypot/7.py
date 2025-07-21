'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hypot\ntorch.Tensor.hypot(_input_tensor, other)\n'
import torch
import torch
input_tensor = torch.randn(4, 4)
other_tensor = torch.randn(4, 4)
hypot_tensor = torch.Tensor.hypot(input_tensor, other_tensor)
print(hypot_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_select\ntorch.Tensor.index_select(_input_tensor, dim, index)\n'
import torch
import torch
input_tensor = torch.randn(4, 4)
dim = 0
index = torch.tensor([0, 2])