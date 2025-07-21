'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_fill_\ntorch.Tensor.index_fill_(_input_tensor, dim, index, value)\n'
import torch
input_tensor = torch.randn(2, 3)
torch.Tensor.index_fill_(input_tensor, 0, torch.LongTensor([0, 1]), 1)
print(input_tensor)
torch.Tensor.index_fill_(input_tensor, 1, torch.LongTensor([0, 1]), 1)
print(input_tensor)