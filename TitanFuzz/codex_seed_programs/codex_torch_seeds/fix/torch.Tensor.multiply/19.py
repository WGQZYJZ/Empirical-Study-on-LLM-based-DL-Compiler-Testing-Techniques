'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.multiply\ntorch.Tensor.multiply(_input_tensor, value)\n'
import torch
input_tensor = torch.randn(2, 3)
value = 2
output_tensor = input_tensor.multiply(value)
print('The input_tensor is:', input_tensor)
print('The value is:', value)
print('The output_tensor is:', output_tensor)