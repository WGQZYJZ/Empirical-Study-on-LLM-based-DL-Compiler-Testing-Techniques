'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.true_divide\ntorch.true_divide(dividend, divisor, *, out)\n'
import torch
a = torch.randn(1, 3, 3, 3)
b = torch.randn(1, 3, 3, 3)
c = torch.true_divide(a, b)
print(c)