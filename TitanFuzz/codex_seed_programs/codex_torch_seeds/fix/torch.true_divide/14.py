'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.true_divide\ntorch.true_divide(dividend, divisor, *, out)\n'
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
y = torch.tensor([[1, 1, 1], [1, 1, 1]], dtype=torch.float32)
print(torch.true_divide(x, y))
print(torch.true_divide(x, 2))
print(torch.true_divide(x, y, out=x))
print(torch.true_divide(x, 2, out=x))