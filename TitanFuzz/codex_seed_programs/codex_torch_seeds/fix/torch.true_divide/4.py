'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.true_divide\ntorch.true_divide(dividend, divisor, *, out)\n'
import torch
input_data = torch.rand(2, 2)
print('Input data:', input_data)
result = torch.true_divide(input_data, 2)
print('Result:', result)