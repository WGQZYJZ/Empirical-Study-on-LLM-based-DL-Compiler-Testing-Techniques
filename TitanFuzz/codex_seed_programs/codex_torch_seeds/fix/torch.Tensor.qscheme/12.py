'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.qscheme\ntorch.Tensor.qscheme(_input_tensor)\n'
import torch
input_data = torch.randn(3, 3)
print('input_data: ', input_data)
output = torch.Tensor.qscheme(input_data)
print('output: ', output)