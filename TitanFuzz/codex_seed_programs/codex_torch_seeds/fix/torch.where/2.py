'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.where\ntorch.where(condition, x, y)\n'
import torch
x = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = torch.tensor([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
condition = (x > 5)
z = torch.where(condition, x, y)
print('x is: ', x)
print('y is: ', y)
print('condition is: ', condition)
print('z is: ', z)