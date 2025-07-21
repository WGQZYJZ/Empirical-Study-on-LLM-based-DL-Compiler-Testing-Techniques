'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.matrix_exp\ntorch.matrix_exp(input)\n'
import torch
import math
input = torch.rand(10, 10, dtype=torch.float64)
print(input)
output = torch.matrix_exp(input)
print(output)