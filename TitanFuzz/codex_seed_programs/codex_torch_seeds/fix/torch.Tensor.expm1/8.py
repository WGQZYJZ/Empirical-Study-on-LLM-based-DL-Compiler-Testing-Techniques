'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.expm1\ntorch.Tensor.expm1(_input_tensor)\n'
import torch
input_data = torch.randn(2, 3)
output_data = torch.Tensor.expm1(input_data)
print('input data: ', input_data)
print('output data: ', output_data)