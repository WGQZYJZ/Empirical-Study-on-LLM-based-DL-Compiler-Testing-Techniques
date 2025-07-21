'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.true_divide\ntorch.true_divide(dividend, divisor, *, out)\n'
import torch
x = torch.tensor([1, 2, 3, 4, 5])
y = torch.tensor([1, 2, 3, 4, 5])
z = torch.true_divide(x, y)
print(z)