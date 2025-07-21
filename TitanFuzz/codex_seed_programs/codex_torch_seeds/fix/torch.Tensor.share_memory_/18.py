'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.share_memory_\ntorch.Tensor.share_memory_(_input_tensor, )\n'
import torch
import numpy as np
_input_tensor = torch.randn(5, 3)
_input_numpy = _input_tensor.numpy()
_input_tensor.share_memory_()
print(_input_tensor)
print(_input_numpy)