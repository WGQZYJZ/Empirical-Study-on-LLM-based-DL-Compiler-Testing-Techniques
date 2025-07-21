'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.true_divide\ntorch.true_divide(dividend, divisor, *, out)\n'
import torch
x = torch.tensor([1, 2, 3, 4])
y = torch.tensor([2, 2, 2, 2])
print(torch.true_divide(x, y))
print(torch.div(x, y))