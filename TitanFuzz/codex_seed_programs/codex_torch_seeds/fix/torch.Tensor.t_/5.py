'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.t_\ntorch.Tensor.t_(_input_tensor)\n'
import torch
import numpy as np
print('Task 1: import PyTorch')
print(torch.__version__)
print('Task 2: Generate input data')
_input_tensor = torch.randn(2, 3, 2)
print(_input_tensor)
print('Task 3: Call the API torch.Tensor.t_')
print(_input_tensor.t_())