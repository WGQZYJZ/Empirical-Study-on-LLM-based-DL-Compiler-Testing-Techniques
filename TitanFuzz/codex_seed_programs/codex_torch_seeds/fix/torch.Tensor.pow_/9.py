'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.pow_\ntorch.Tensor.pow_(_input_tensor, exponent)\n'
import torch
input_data = torch.randn(2, 3)
print('input_data: ', input_data)
result = torch.Tensor.pow_(input_data, 2)
print('result: ', result)