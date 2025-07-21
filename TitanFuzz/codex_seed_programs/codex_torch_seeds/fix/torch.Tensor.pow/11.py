'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.pow\ntorch.Tensor.pow(_input_tensor, exponent)\n'
import torch
input_tensor = torch.randn(1, 3)
print('Input: ', input_tensor)
output_tensor = torch.Tensor.pow(input_tensor, 2)
print('Output: ', output_tensor)