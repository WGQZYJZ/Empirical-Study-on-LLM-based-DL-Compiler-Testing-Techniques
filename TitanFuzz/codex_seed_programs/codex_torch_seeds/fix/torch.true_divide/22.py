'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.true_divide\ntorch.true_divide(dividend, divisor, *, out)\n'
import torch
input_data = torch.randn(4, 4)
divisor = torch.tensor([2, 2, 2, 2])
output = torch.true_divide(input_data, divisor)
print(output)