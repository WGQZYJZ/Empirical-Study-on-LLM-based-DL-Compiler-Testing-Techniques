'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.heaviside\ntorch.Tensor.heaviside(_input_tensor, values)\n'
import torch
import numpy as np
_input_tensor = torch.tensor([[(- 1), 0, 1], [1, 0, (- 1)]])
print('Input tensor: ')
print(_input_tensor)
print('Result tensor: ')
print(torch.Tensor.heaviside(_input_tensor, values=0.5))