'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.count_nonzero\ntorch.Tensor.count_nonzero(_input_tensor, dim=None)\n'
import torch
_input_tensor = torch.randn(2, 3, 4)
count_nonzero = torch.Tensor.count_nonzero(_input_tensor, dim=None)
print('count_nonzero: ', count_nonzero)