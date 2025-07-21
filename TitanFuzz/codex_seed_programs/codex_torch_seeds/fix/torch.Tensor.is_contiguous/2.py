'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_contiguous\ntorch.Tensor.is_contiguous(_input_tensor, memory_format=torch.contiguous_format)\n'
import torch
import numpy as np
_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(_input_tensor)
print(_input_tensor.is_contiguous())