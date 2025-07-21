'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.var\ntorch.var(input, dim, unbiased, keepdim=False, *, out=None)\n'
import torch
import numpy as np
input_data = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
print(torch.var(input_data, 0, True))
print(torch.var(input_data, 1, True))
print(torch.var(input_data, 0, False))
print(torch.var(input_data, 1, False))
print(torch.var(input_data, 0, True, True))
print(torch.var(input_data, 1, True, True))
print(torch.var(input_data, 0, False, True))
print(torch.var(input_data, 1, False, True))