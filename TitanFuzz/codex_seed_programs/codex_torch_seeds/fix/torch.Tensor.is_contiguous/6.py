'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_contiguous\ntorch.Tensor.is_contiguous(_input_tensor, memory_format=torch.contiguous_format)\n'
import torch
import numpy as np
_input_tensor = torch.arange(0, 6).view(2, 3)
print(_input_tensor)
print(_input_tensor.is_contiguous())