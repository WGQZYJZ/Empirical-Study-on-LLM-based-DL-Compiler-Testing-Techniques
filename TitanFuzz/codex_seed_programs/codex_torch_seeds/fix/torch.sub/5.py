'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sub\ntorch.sub(input, other, *, alpha=1, out=None)\n'
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
y = torch.tensor([[1, 1, 1], [2, 2, 2]])
print(torch.sub(x, y))
print(x.sub(y))
print((x - y))