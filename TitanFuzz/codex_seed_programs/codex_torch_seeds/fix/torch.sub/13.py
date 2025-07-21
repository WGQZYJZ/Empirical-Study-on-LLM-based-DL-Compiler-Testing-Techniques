'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sub\ntorch.sub(input, other, *, alpha=1, out=None)\n'
import torch
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
y = torch.tensor([[1, 1, 1], [1, 1, 1]])
z = torch.sub(x, y)
print(z)
z = torch.sub(x, y, out=torch.empty(x.shape))
print(z)
z = torch.sub(x, y, alpha=2)
print(z)
z = torch.sub(x, y, alpha=2, out=torch.empty(x.shape))
print(z)