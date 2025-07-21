'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.matrix_exp\ntorch.Tensor.matrix_exp(_input_tensor)\n'
import torch
_input_tensor = torch.Tensor([[1, 2], [3, 4]])
_output_tensor = _input_tensor.matrix_exp()
print('Input Tensor:\n', _input_tensor)
print('Output Tensor:\n', _output_tensor)