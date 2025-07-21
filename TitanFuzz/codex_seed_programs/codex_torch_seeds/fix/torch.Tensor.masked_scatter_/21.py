'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_scatter_\ntorch.Tensor.masked_scatter_(_input_tensor, mask, source\n'
import torch
input_tensor = torch.Tensor([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
mask = torch.Tensor([[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]])
source = torch.Tensor([[100, 101, 102, 103], [104, 105, 106, 107], [108, 109, 110, 111]])
print(input_tensor.masked_scatter_(mask, source))