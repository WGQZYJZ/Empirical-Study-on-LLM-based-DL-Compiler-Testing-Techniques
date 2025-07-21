'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arcsin_\ntorch.Tensor.arcsin_(_input_tensor)\n'
import torch
input_data = torch.randn(1, 3)
print('Input data: ', input_data)
output = torch.Tensor.arcsin_(input_data)
print('Output data: ', output)