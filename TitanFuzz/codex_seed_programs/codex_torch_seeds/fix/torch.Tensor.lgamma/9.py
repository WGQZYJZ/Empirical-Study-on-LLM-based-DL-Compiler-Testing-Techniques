'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lgamma\ntorch.Tensor.lgamma(_input_tensor)\n'
import torch
input_tensor = torch.rand(2, 3)
print('Input Tensor: ', input_tensor)
output_tensor = torch.Tensor.lgamma(input_tensor)
print('Output Tensor: ', output_tensor)