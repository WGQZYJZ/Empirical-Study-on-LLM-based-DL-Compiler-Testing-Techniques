'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hypot_\ntorch.Tensor.hypot_(_input_tensor, other)\n'
import torch
import torch
input_tensor = torch.arange(0, 4, dtype=torch.float32)
other = torch.tensor([2], dtype=torch.float32)
output = torch.Tensor.hypot_(input_tensor, other)
print(input_tensor)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_select_\ntorch.Tensor.index_select_(input, dim, index)\n'
import torch
import torch
input_tensor = torch.arange(0, 12, dtype=torch.float32).reshape(3, 4)
index = torch.tensor([1, 0])