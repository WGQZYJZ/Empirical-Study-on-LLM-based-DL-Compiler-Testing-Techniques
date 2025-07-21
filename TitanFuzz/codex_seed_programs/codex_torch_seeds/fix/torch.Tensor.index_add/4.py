'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_add\ntorch.Tensor.index_add(_input_tensor, dim, index, tensor2)\n'
import torch
input_tensor = torch.randn(4, 4)
index = torch.tensor([0, 2])
src = torch.randn(2, 4)
torch.Tensor.index_add(input_tensor, dim=0, index=index, tensor=src)
print('input_tensor: {}'.format(input_tensor))