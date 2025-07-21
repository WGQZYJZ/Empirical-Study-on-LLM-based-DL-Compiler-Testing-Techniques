'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_scatter_\ntorch.Tensor.masked_scatter_(_input_tensor, mask, source\n'
import torch
input_tensor = torch.randn(2, 3, 3)
mask = torch.tensor([[0, 0, 1], [0, 1, 0]])
source = torch.tensor([[1, 2, 3], [4, 5, 6]])
torch.Tensor.masked_scatter_(input_tensor, mask, source)
print(input_tensor)