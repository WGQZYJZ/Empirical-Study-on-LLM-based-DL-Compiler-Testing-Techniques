'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.histc\ntorch.Tensor.histc(_input_tensor, bins=100, min=0, max=0)\n'
import torch
import numpy as np
_input_tensor = torch.rand(100)
_output_tensor = torch.Tensor.histc(_input_tensor, bins=100, min=0, max=0)
print(_output_tensor)