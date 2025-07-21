'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_scatter_\ntorch.Tensor.masked_scatter_(_input_tensor, mask, source\n'
import torch
import torch
input_tensor = torch.rand(3, 3)
mask = torch.tensor([[1, 0, 1], [1, 1, 0], [0, 0, 1]], dtype=torch.uint8)
source = torch.rand(3, 3)
torch.Tensor.masked_scatter_(input_tensor, mask, source)
print(input_tensor)