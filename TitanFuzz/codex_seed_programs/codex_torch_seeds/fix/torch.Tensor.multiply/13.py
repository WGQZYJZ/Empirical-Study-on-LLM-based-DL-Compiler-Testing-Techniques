'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.multiply\ntorch.Tensor.multiply(_input_tensor, value)\n'
import torch
input_tensor = torch.randn(1, 3, 3, 3)
value = 2
output_tensor = torch.Tensor.multiply(input_tensor, value)
print('The output tensor is: ', output_tensor)