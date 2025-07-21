'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.floor_divide\ntorch.Tensor.floor_divide(_input_tensor, value)\n'
import torch
input_tensor = torch.randn(10)
print('Input tensor: {}'.format(input_tensor))
result = torch.Tensor.floor_divide(input_tensor, 5)
print('Result: {}'.format(result))