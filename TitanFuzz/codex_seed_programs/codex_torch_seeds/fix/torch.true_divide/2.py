'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.true_divide\ntorch.true_divide(dividend, divisor, *, out)\n'
import torch
import torch
input_data = torch.randn(2, 3)
print('input_data: ', input_data)
output_data = torch.true_divide(input_data, 0.5)
print('output_data: ', output_data)