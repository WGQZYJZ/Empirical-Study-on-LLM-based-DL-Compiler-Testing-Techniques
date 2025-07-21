'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.matrix_power\ntorch.Tensor.matrix_power(_input_tensor, n)\n'
import torch
import torch
input_tensor = torch.randn(4, 4)
print('Input tensor: ', input_tensor)
result = torch.Tensor.matrix_power(input_tensor, 2)
print('Result: ', result)