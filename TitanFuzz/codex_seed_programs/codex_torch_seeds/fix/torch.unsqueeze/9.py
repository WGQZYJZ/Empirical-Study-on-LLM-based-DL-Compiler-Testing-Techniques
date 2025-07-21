'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unsqueeze\ntorch.unsqueeze(input, dim)\n'
import torch
a = torch.Tensor([[1, 2, 3], [4, 5, 6]])
print(a)
b = torch.unsqueeze(a, dim=0)
print(b)
c = torch.unsqueeze(a, dim=1)
print(c)
d = torch.unsqueeze(a, dim=2)
print(d)
e = torch.unsqueeze(a, dim=(- 1))
print(e)
f = torch.unsqueeze(a, dim=(- 2))
print(f)