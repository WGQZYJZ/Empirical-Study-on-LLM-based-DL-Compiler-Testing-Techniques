'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_scatter_\ntorch.Tensor.masked_scatter_(_input_tensor, mask, source\n'
import torch
_input_tensor = torch.randn((4, 4))
mask = torch.ByteTensor([[1, 0, 0, 1], [0, 0, 0, 1], [1, 1, 1, 1], [0, 0, 0, 0]])
source = torch.randn((4, 4))
torch.Tensor.masked_scatter_(_input_tensor, mask, source)
print(_input_tensor)