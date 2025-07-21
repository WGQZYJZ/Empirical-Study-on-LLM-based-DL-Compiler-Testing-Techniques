'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.eq\ntorch.eq(input, other, *, out=None)\n'
import torch
import torch
input = torch.randint(0, 10, (3, 3), dtype=torch.float32)
print('Input: ', input)
output = torch.eq(input, 5)
print('Output: ', output)