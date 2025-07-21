'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.true_divide\ntorch.true_divide(dividend, divisor, *, out)\n'
import torch
a = torch.rand(3, 3)
b = torch.rand(3, 3)
print('Input:')
print('a:', a)
print('b:', b)
print('Output:')
print('torch.true_divide(a, b):', torch.true_divide(a, b))