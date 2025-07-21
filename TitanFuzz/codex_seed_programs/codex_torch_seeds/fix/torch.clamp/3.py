'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clamp\ntorch.clamp(input, min=None, max=None, *, out=None)\n'
import torch
x = torch.randn(4, 4)
print(x)
print(x.size())
print('\nTask 2: Generate input data')
min_value = (- 0.5)
max_value = 0.5
print(('min_value = %.2f' % min_value))
print(('max_value = %.2f' % max_value))
print('\nTask 3: Call the API torch.clamp')
y = torch.clamp(x, min=min_value, max=max_value)
print(y)