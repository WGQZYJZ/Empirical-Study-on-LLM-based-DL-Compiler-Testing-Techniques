'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.multiply\ntorch.Tensor.multiply(_input_tensor, value)\n'
import torch
input_tensor = torch.ones((2, 2))
print('Input tensor: ', input_tensor)
result = torch.Tensor.multiply(input_tensor, 10)
print('Result: ', result)