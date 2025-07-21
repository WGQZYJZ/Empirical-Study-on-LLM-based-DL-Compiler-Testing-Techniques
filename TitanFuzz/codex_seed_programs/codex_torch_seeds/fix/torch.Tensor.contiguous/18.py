'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.contiguous\ntorch.Tensor.contiguous(_input_tensor, memory_format=torch.contiguous_format)\n'
import torch
import numpy as np
'\nTask 1: import PyTorch\n'
import torch
'\nTask 2: Generate input data\n'
_input_tensor = torch.randn(2, 3, 4, 5)
'\nTask 3: Call the API torch.Tensor.contiguous\ntorch.Tensor.contiguous(_input_tensor, memory_format=torch.contiguous_format)\n'
output_tensor = _input_tensor.contiguous()
print(output_tensor)