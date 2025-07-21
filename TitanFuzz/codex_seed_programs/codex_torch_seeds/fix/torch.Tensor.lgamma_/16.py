'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lgamma_\ntorch.Tensor.lgamma_(_input_tensor)\n'
import torch
input_data = torch.randn(5, 3)
print('Input data:\n', input_data)
output = torch.Tensor.lgamma_(input_data)
print('Output:\n', output)