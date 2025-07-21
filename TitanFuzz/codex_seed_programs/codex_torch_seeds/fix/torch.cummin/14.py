'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cummin\ntorch.cummin(input, dim, *, out=None)\n'
import torch
input = torch.randint(0, 10, (3, 3))
print(f'input data: {input}')
print(f'cummin along axis 0: {torch.cummin(input, 0)}')
print(f'cummin along axis 1: {torch.cummin(input, 1)}')