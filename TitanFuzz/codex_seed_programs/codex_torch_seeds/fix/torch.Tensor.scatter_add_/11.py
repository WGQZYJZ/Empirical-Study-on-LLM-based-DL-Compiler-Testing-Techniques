'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_add_\ntorch.Tensor.scatter_add_(_input_tensor, dim, index, src)\n'
import torch
import numpy as np
input_tensor = torch.randn(2, 3)
index = torch.tensor([[0, 1], [1, 0]])
src = torch.randn(2, 2)
output_tensor = torch.Tensor.scatter_add_(input_tensor, dim=0, index=index, src=src)
print(input_tensor)
print(output_tensor)