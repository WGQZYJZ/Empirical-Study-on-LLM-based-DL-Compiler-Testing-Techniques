'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arctan\ntorch.Tensor.arctan(_input_tensor)\n'
import torch
input_data = torch.randn(1)
output = torch.Tensor.arctan(input_data)
print('input_data: ', input_data)
print('output: ', output)