'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill\ntorch.Tensor.masked_fill(_input_tensor, mask, value)\n'
import torch
import torch
input_tensor = torch.rand(3, 3)
mask = torch.tensor([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
value = torch.tensor(1.0)
result = torch.Tensor.masked_fill(input_tensor, mask, value)
print(result)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_scatter\ntorch.Tensor.masked_scatter(_input_tensor, mask, source)\n'
import torch
import torch
input_tensor = torch.rand(3, 3)