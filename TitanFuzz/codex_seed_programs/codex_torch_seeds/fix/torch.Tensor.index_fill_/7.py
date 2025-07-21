'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_fill_\ntorch.Tensor.index_fill_(_input_tensor, dim, index, value)\n'
import torch
input_tensor = torch.randn(4, 4)
print(input_tensor)
torch.Tensor.index_fill_(input_tensor, 1, torch.tensor([0, 2]), 2.0)
print(input_tensor)