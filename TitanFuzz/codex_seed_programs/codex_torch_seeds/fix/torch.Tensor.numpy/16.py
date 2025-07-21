'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.numpy\ntorch.Tensor.numpy(_input_tensor)\n'
import torch
import numpy as np
_input_tensor = torch.randn((1, 2, 3, 4))
_output_numpy = _input_tensor.numpy()
print(_output_numpy)