'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arctan\ntorch.arctan(input, *, out=None)\n'
import torch
x = torch.tensor([0, 30, 45, 60, 90])
print('Input: ', x)
y = torch.arctan(x.float())
print('Output: ', y)