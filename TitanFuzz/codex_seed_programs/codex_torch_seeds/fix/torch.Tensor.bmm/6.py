'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bmm\ntorch.Tensor.bmm(_input_tensor, batch2)\n'
import torch
import torch
_input_tensor = torch.rand(10, 3, 4)
batch2 = torch.rand(10, 4, 5)
torch.Tensor.bmm(_input_tensor, batch2)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.chunk\ntorch.Tensor.chunk(_input_tensor, chunks, dim)\n'
import torch
import torch
_input_tensor = torch.rand(10, 3, 4)
chunks = 3
dim = 1
torch.Tensor.chunk(_input_tensor, chunks, dim)