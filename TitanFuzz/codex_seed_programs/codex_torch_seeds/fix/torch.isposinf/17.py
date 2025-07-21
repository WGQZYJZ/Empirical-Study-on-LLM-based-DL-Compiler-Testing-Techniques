'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isposinf\ntorch.isposinf(input, *, out=None)\n'
import torch
input = torch.randn(4, 4)
input[0][0] = float('inf')
input[1][0] = float('-inf')
input[2][0] = float('nan')
input[3][0] = float('nan')
output = torch.isposinf(input)
print('Output: ', output)