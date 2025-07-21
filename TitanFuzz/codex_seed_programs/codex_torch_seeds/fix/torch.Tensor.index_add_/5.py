'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_add_\ntorch.Tensor.index_add_(_input_tensor, dim, index, tensor, *, alpha=1)\n'
import torch
import torch
_input_tensor = torch.rand(2, 3, 4)
_dim = 1
_index = torch.tensor([0, 2])
_tensor = torch.rand(2, 4)
torch.Tensor.index_add_(_input_tensor, _dim, _index, _tensor)
print(_input_tensor)