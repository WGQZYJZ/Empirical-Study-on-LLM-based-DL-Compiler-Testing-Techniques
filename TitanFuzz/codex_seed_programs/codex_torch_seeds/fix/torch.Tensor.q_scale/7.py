'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_scale\ntorch.Tensor.q_scale(_input_tensor)\n'
import torch
import torch.nn as nn
_input_tensor = torch.rand(2, 3, 4, 5)
_output_tensor = _input_tensor.q_scale()
print(_output_tensor)