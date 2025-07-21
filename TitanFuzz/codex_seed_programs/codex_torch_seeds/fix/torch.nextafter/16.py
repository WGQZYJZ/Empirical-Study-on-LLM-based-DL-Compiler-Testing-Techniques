'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nextafter\ntorch.nextafter(input, other, *, out=None)\n'
import torch
x = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
y = torch.nextafter(x, torch.tensor([0.0, 1.0, 2.0, 3.0, 4.0]))
print('Input data:')
print(x)
print('Output data:')
print(y)