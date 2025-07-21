'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.round\ntorch.Tensor.round(_input_tensor)\n'
import torch
_input_tensor = torch.Tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
_output_tensor = _input_tensor.round()
print('Input Tensor: {}'.format(_input_tensor))
print('Output Tensor: {}'.format(_output_tensor))