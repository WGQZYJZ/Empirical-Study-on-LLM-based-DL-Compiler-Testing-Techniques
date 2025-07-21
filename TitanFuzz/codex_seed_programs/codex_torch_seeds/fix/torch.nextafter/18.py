'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nextafter\ntorch.nextafter(input, other, *, out=None)\n'
import torch
import torch
x = torch.tensor([1.0, 2.0, 3.0])
y = torch.tensor([3.0, 2.0, 1.0])
z = torch.nextafter(x, y)
print('The result of torch.nextafter(x, y) = ', z)