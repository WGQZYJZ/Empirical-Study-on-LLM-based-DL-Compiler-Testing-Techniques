'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.true_divide\ntorch.true_divide(dividend, divisor, *, out)\n'
import torch
dividend = torch.randn(2, 3)
divisor = torch.randn(2, 3)
true_divide = torch.true_divide(dividend, divisor)
print('Input 1:')
print(dividend)
print('Input 2:')
print(divisor)
print('Output:')
print(true_divide)