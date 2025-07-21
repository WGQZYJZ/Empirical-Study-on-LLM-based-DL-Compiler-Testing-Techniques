'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.triu_\ntorch.Tensor.triu_(_input_tensor, diagonal=0)\n'
import torch
input_tensor = torch.arange(1, 13).view(3, 4)
print('Input tensor: ', input_tensor)
output_tensor = input_tensor.triu_(diagonal=0)
print('Output tensor: ', output_tensor)