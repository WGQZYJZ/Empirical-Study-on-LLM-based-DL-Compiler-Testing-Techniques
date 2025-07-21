'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gather\ntorch.Tensor.gather(_input_tensor, dim, index)\n'
import torch
import torch
input_tensor = torch.randn(2, 3)
print(input_tensor)
index = torch.tensor([[0, 1], [1, 0]])
print(input_tensor.gather(0, index))
index = torch.tensor([[0, 1], [1, 0]])
print(input_tensor.gather(1, index))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_select\ntorch.Tensor.index_select(_input_tensor, dim, index)\n'
import torch
import torch
input_tensor = torch.randn(2, 3)
print(input_tensor)