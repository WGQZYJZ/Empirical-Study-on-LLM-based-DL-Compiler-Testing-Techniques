'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lerp\ntorch.lerp(input, end, weight, *, out=None)\n'
import torch
import torch
x = torch.rand(4, 4)
y = torch.rand(4, 4)
z = torch.rand(4, 4)
output = torch.lerp(x, y, z)
print(output)