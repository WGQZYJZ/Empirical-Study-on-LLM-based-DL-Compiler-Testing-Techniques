'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_scatter_\ntorch.Tensor.masked_scatter_(_input_tensor, mask, source\n'
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
mask = torch.ByteTensor([[0, 1, 1], [1, 1, 0]])
source = torch.Tensor([[7, 8, 9], [10, 11, 12]])
torch.Tensor.masked_scatter_(input_tensor, mask, source)
print(input_tensor)