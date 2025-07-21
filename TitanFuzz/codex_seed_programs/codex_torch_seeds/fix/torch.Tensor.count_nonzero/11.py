'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.count_nonzero\ntorch.Tensor.count_nonzero(_input_tensor, dim=None)\n'
import torch
import numpy as np
_input_tensor = torch.tensor([[0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]])
_output_tensor = torch.Tensor.count_nonzero(_input_tensor, dim=None)
print('All non-zero elements: ', _output_tensor)
_output_tensor = torch.Tensor.count_nonzero(_input_tensor, dim=0)
print('Non-zero elements in each column: ', _output_tensor)
_output_tensor = torch.Tensor.count_nonzero(_input_tensor, dim=1)
print('Non-zero elements in each row: ', _output_tensor)