'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unsqueeze\ntorch.unsqueeze(input, dim)\n'
import torch
x = torch.Tensor([1, 2, 3, 4])
print(x)
print(x.shape)
y = torch.unsqueeze(x, dim=0)
print(y)
print(y.shape)
z = torch.unsqueeze(x, dim=1)
print(z)
print(z.shape)