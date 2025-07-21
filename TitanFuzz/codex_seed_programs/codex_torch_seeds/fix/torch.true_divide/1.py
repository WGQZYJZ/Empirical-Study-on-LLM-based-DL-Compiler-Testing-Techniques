'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.true_divide\ntorch.true_divide(dividend, divisor, *, out)\n'
import torch
a = torch.rand(2, 3)
b = torch.rand(2, 3)
print(torch.true_divide(a, b))