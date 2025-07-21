'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ge\ntorch.ge(input, other, *, out=None)\n'
import torch
input = torch.randn(3, 3)
print('Input data: \n', input)
print('Input data type: \n', input.type())
print('Torch GE: \n', torch.ge(input, 0))
'\nTask 4: Call the API torch.gt\ntorch.gt(input, other, *, out=None)\n'
print('Torch GT: \n', torch.gt(input, 0))
'\nTask 5: Call the API torch.le\ntorch.le(input, other, *, out=None)\n'
print('Torch LE: \n', torch.le(input, 0))
'\nTask 6: Call the API torch.lt\ntorch.lt(input, other, *, out=None)\n'
print('Torch LT: \n', torch.lt(input, 0))
'\nTask 7: Call the API torch.eq\ntorch.eq(input, other, *, out=None)\n'