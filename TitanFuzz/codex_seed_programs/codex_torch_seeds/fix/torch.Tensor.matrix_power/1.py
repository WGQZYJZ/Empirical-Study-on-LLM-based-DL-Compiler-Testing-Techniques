'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.matrix_power\ntorch.Tensor.matrix_power(_input_tensor, n)\n'
import torch
_input_tensor = torch.randn(2, 2)
n = 2
_output_tensor = _input_tensor.matrix_power(n)
print('The input tensor is:', _input_tensor)
print('The output tensor is:', _output_tensor)