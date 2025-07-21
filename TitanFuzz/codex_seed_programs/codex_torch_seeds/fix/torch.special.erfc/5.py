'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.erfc\ntorch.special.erfc(input, *, out=None)\n'
import torch
x = torch.tensor([0.3, 0.5, 0.7])
y = torch.special.erfc(x)
print('Input: ', x)
print('Output: ', y)