'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.true_divide\ntorch.true_divide(dividend, divisor, *, out)\n'
import torch
dividend = torch.tensor([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
divisor = torch.tensor([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
output = torch.true_divide(dividend, divisor)
print('output = ', output)