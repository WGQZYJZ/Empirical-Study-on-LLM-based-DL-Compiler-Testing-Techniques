'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isposinf\ntorch.isposinf(input, *, out=None)\n'
import torch
import numpy as np
a = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
b = torch.tensor([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
print(torch.isposinf(a))
print(torch.isposinf(b))