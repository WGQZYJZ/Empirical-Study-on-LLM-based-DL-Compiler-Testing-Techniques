'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.negative_\ntorch.Tensor.negative_(_input_tensor)\n'
import torch
import numpy as np
_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
expected_output_tensor = torch.tensor([[(- 1), (- 2), (- 3)], [(- 4), (- 5), (- 6)]])
output_tensor = _input_tensor.negative_()
print('Input tensor: ', _input_tensor)
print('Expected output tensor: ', expected_output_tensor)
print('Actual output tensor: ', output_tensor)
print('Input tensor: ', _input_tensor)
print('Expected output tensor: ', expected_output_tensor)
print('Actual output tensor: ', output_tensor)