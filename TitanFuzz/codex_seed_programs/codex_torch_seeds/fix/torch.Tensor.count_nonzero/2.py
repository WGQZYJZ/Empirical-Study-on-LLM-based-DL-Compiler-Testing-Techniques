'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.count_nonzero\ntorch.Tensor.count_nonzero(_input_tensor, dim=None)\n'
import torch
import torch
_input_tensor = torch.tensor([[1, 0, 1, 1, 0], [1, 1, 1, 0, 0]])
print(_input_tensor.count_nonzero())
print(_input_tensor.count_nonzero(dim=0))
print(_input_tensor.count_nonzero(dim=1))
print(_input_tensor.nonzero())
print(_input_tensor.nonzero(as_tuple=True))