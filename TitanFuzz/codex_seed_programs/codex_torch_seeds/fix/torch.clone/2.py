'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clone\ntorch.clone(input, *, memory_format=torch.preserve_format)\n'
import torch
x = torch.ones(5, 5)
print(x)
y = torch.clone(x)
print(y)
y.fill_(2)
print(x)
print(y)