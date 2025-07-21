'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.matrix_power\ntorch.Tensor.matrix_power(_input_tensor, n)\n'
import torch
import torch
_input_tensor = torch.arange(1, 10).view(3, 3)
print('_input_tensor = ', _input_tensor)
print('_input_tensor.matrix_power(2) = ', _input_tensor.matrix_power(2))