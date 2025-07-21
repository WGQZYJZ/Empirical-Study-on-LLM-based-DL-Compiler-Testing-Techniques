'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_and\ntorch.Tensor.logical_and(_input_tensor, other)\n'
import torch
_input_tensor = torch.tensor([[True, True], [False, False]])
_output_tensor = _input_tensor.logical_and(False)
print('input_tensor:', _input_tensor)
print('output_tensor:', _output_tensor)