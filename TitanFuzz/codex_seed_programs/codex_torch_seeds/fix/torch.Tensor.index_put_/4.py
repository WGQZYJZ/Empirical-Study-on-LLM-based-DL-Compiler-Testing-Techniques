'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_put_\ntorch.Tensor.index_put_(_input_tensor, indices, values, accumulate=False)\n'
import torch
import numpy as np
input_tensor = torch.rand(3, 5)
indices = torch.tensor([[0, 1], [2, 3]])
values = torch.tensor([[0.1, 0.2], [0.3, 0.4]])
output = torch.Tensor.index_put_(input_tensor, indices, values)
print(output)