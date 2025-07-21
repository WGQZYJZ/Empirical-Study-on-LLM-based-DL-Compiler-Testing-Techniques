'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arccosh_\ntorch.Tensor.arccosh_(_input_tensor, )\n'
import torch
input_data = torch.randn(1, 3, 3)
output = torch.Tensor.arccosh_(input_data)
print('Input: ', input_data)
print('Output: ', output)