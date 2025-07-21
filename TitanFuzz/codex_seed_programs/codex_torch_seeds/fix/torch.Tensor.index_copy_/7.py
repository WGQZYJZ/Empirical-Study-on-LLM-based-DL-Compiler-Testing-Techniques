'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_copy_\ntorch.Tensor.index_copy_(_input_tensor, dim, index, tensor)\n'
import torch
import torch
input_tensor = torch.arange(0, 12).reshape(3, 4)
print('input_tensor: ', input_tensor)
torch.Tensor.index_copy_(input_tensor, dim=0, index=torch.tensor([0, 2]), tensor=torch.tensor([100, 200]))
print('after index_copy_: ', input_tensor)