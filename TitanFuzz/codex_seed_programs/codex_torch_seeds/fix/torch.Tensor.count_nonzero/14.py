'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.count_nonzero\ntorch.Tensor.count_nonzero(_input_tensor, dim=None)\n'
import torch
_input_tensor = torch.randint(low=0, high=2, size=(2, 3, 4))
print(_input_tensor)
print(_input_tensor.count_nonzero())
print(_input_tensor.count_nonzero(dim=0))
print(_input_tensor.count_nonzero(dim=1))
print(_input_tensor.count_nonzero(dim=2))