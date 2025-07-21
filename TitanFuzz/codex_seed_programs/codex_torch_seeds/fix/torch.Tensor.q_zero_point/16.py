'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_zero_point\ntorch.Tensor.q_zero_point(_input_tensor)\n'
import torch
import numpy as np
_input_tensor = torch.Tensor([1.0, 2.0, 3.0, 4.0])
_zero_point = _input_tensor.q_zero_point()
print(_zero_point)