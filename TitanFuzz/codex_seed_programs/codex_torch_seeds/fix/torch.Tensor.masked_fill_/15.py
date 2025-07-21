'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill_\ntorch.Tensor.masked_fill_(_input_tensor, mask, value\n'
import torch
input_tensor = torch.rand(10, 10)
mask = torch.rand(10, 10)
value = torch.rand(1)
torch.Tensor.masked_fill_(input_tensor, mask, value)