'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.multiply\ntorch.Tensor.multiply(_input_tensor, value)\n'
import torch
input_tensor = torch.rand(2, 3)
print('Input tensor: ', input_tensor)
result_tensor = torch.Tensor.multiply(input_tensor, 2)
print('Result tensor: ', result_tensor)