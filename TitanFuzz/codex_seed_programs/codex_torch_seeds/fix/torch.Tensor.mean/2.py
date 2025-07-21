'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mean\ntorch.Tensor.mean(_input_tensor, dim=None, keepdim=False, *, dtype=None)\n'
import torch
_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
_mean_value = _input_tensor.mean(dim=1)
print('The mean value is: ', _mean_value)