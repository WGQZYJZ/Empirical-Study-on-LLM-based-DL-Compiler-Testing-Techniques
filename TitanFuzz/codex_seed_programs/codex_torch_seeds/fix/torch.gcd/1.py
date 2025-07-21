'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.gcd\ntorch.gcd(input, other, *, out=None)\n'
import torch
import numpy as np
print('\n Task 1')
print('PyTorch version: ', torch.__version__)
print('CUDA Available: ', torch.cuda.is_available())
print('\n Task 2')
input = torch.tensor([24, 60], dtype=torch.int32)
print('Input: ', input)
print('\n Task 3')
out = torch.gcd(input[0], input[1])
print('GCD of ', input[0], ' and ', input[1], ' is ', out)