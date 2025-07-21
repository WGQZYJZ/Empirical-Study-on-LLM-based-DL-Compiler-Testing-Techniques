'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.neg\ntorch.neg(input, *, out=None)\n'
import torch
x = torch.randn(4, 4)
print(x)
print(torch.neg(x))
'\nTask 4: Call the API torch.add\ntorch.add(input, value, *, out=None)\n'
x = torch.randn(4, 4)
print(x)
print(torch.add(x, x))
'\nTask 5: Call the API torch.sub\ntorch.sub(input, other, *, out=None)\n'
x = torch.randn(4, 4)
print(x)
print(torch.sub(x, x))
'\nTask 6: Call the API torch.mul\ntorch.mul(input, other, *, out=None)\n'
x = torch.randn(4, 4)
print(x)
print(torch.mul(x, x))
'\nTask 7: Call the API torch.div\ntorch.div(input, other, *, out=None)\n'