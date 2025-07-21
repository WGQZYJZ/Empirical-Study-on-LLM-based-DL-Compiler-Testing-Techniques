'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.triu_\ntorch.Tensor.triu_(_input_tensor, diagonal=0)\n'
import torch
input_tensor = torch.rand(1, 2, 3)
print('Input tensor: \n', input_tensor)
output_tensor = input_tensor.triu_(diagonal=0)
print('Output tensor: \n', output_tensor)
output_tensor = input_tensor.triu_(diagonal=1)
print('Output tensor: \n', output_tensor)
output_tensor = input_tensor.triu_(diagonal=2)
print('Output tensor: \n', output_tensor)