'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cummin\ntorch.Tensor.cummin(_input_tensor, dim)\n'
import torch
import numpy as np
_input_tensor = torch.randint(0, 10, (3, 4))
_output_tensor = _input_tensor.cummin(dim=1)
print(_output_tensor)