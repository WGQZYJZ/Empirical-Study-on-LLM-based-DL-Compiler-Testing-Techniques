'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isposinf\ntorch.isposinf(input, *, out=None)\n'
import torch
x = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(torch.isposinf(x))
x = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], dtype=torch.float)
print(torch.isposinf(x))
x = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], dtype=torch.double)
print(torch.isposinf(x))
x = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], dtype=torch.half)
print(torch.isposinf(x))
x = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], dtype=torch.bool)