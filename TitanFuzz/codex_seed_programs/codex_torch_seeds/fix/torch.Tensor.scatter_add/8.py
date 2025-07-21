'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_add\ntorch.Tensor.scatter_add(_input_tensor, dim, index, src)\n'
import torch
import torch.nn as nn
import torch
_input_tensor = torch.randn(5, 5)
_index = torch.tensor([[4, 3, 1], [3, 2, 0]])
_src = torch.tensor([[1, 0, 1], [1, 1, 0]], dtype=torch.float)
output = torch.Tensor.scatter_add(_input_tensor, dim=1, index=_index, src=_src)
print(output)