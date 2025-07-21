'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_put_\ntorch.Tensor.index_put_(_input_tensor, indices, values, accumulate=False)\n'
import torch
import numpy as np
_input_tensor = torch.randn(3, 4)
indices = torch.tensor([[0, 1], [1, 2]])
values = torch.tensor([[2, 3], [4, 5]])
_input_tensor.index_put_(_input_tensor, indices, values, accumulate=False)
print(_input_tensor)