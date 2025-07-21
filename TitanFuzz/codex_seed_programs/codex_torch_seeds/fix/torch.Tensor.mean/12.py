'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mean\ntorch.Tensor.mean(_input_tensor, dim=None, keepdim=False, *, dtype=None)\n'
import torch
_input_data = torch.rand(4, 4)
print(_input_data)
mean_value = torch.Tensor.mean(_input_data, dim=1)
print(mean_value)