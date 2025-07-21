'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_not\ntorch.bitwise_not(input, *, out=None)\n'
import torch
input = torch.tensor([[1, 0, 0], [0, 1, 0]], dtype=torch.bool)
print('Input data: ', input)
result = torch.bitwise_not(input)
print('Result: ', result)