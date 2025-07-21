'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arctan\ntorch.arctan(input, *, out=None)\n'
import torch
a = torch.randn(1, requires_grad=True)
print('a =', a)
result = torch.arctan(a)
print('result =', result)
result.backward()
print('gradients =', a.grad)