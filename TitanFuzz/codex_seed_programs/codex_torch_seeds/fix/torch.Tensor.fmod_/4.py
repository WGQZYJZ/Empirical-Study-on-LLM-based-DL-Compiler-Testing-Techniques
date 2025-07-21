'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fmod_\ntorch.Tensor.fmod_(_input_tensor, divisor)\n'
import torch
import numpy as np
input_tensor = torch.rand(3, 3)
divisor = torch.tensor(2)
torch.Tensor.fmod_(input_tensor, divisor)
print('input_tensor: ', input_tensor)
'\ntorch.Tensor.fmod_(_input_tensor, divisor)\nParameters:\n    _input_tensor (Tensor) – the tensor to be modified\n    divisor (Tensor or float) – the divisor\nReturns:\n    Tensor – the result tensor\n'