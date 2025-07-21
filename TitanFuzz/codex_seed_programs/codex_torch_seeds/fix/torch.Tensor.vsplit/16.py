'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.vsplit\ntorch.Tensor.vsplit(_input_tensor, split_size_or_sections)\n'
import torch
import numpy as np
input_tensor = torch.randn(2, 6)
print('input_tensor = {}'.format(input_tensor))
split_tensor = torch.Tensor.vsplit(input_tensor, 3)
print('split_tensor = {}'.format(split_tensor))