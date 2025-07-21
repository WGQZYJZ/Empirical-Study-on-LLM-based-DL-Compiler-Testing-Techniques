'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.trunc\ntorch.Tensor.trunc(_input_tensor)\n'
import torch
import numpy as np
_input_tensor = torch.tensor([[1.5, 2.5, 3.5, 4.5], [5.5, 6.5, 7.5, 8.5], [9.5, 10.5, 11.5, 12.5]])
_output_tensor = torch.Tensor.trunc(_input_tensor)
print('Input tensor:')
print(_input_tensor)
print('Output tensor:')
print(_output_tensor)