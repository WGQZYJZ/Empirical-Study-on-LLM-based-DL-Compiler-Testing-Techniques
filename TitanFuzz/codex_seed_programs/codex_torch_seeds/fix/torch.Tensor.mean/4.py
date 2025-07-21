'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mean\ntorch.Tensor.mean(_input_tensor, dim=None, keepdim=False, *, dtype=None)\n'
import torch
_input_tensor = torch.rand(10, 3)
mean_value = _input_tensor.mean()
print(mean_value)
mean_value = _input_tensor.mean(dim=0)
print(mean_value)
mean_value = _input_tensor.mean(dim=1)
print(mean_value)
mean_value = _input_tensor.mean(dim=1, keepdim=True)
print(mean_value)