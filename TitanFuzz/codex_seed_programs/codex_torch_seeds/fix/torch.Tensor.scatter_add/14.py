'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_add\ntorch.Tensor.scatter_add(_input_tensor, dim, index, src)\n'
import torch
import numpy as np
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
index = torch.tensor([[0, 1, 2], [2, 0, 0]])
src = torch.tensor([[2, 3, 4], [5, 6, 7]])
output_tensor = torch.Tensor.scatter_add(input_tensor, dim=0, index=index, src=src)
print(output_tensor)