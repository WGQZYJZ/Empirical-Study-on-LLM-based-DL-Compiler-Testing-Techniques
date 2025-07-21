'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.triu\ntorch.triu(input, diagonal=0, *, out=None)\n'
import torch
x = torch.arange(1, 10).view(3, 3)
print(x)
print(torch.triu(x))
print(torch.triu(x, diagonal=1))
print(torch.triu(x, diagonal=2))
y = torch.ones(3, 3)
print(torch.triu(y, diagonal=1))
print(torch.tril(x))
print(torch.tril(x, diagonal=1))
print(torch.tril(x, diagonal=2))
print(torch.tril(y, diagonal=1))