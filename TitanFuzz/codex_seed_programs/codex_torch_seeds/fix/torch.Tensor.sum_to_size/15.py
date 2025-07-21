'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sum_to_size\ntorch.Tensor.sum_to_size(_input_tensor, *size)\n'
import torch
_input_tensor = torch.randn(2, 3, 4)
_size = (4, 4)
_output_tensor = torch.Tensor.sum_to_size(_input_tensor, *_size)
print('input: {}'.format(_input_tensor))
print('output: {}'.format(_output_tensor))