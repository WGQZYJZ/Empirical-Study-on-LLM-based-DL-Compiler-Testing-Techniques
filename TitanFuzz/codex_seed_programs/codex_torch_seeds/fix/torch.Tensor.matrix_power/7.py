'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.matrix_power\ntorch.Tensor.matrix_power(_input_tensor, n)\n'
import torch
_input_tensor = torch.rand(2, 2)
_output_tensor = torch.Tensor.matrix_power(_input_tensor, 2)
print('Input tensor: ', _input_tensor)
print('Output tensor: ', _output_tensor)