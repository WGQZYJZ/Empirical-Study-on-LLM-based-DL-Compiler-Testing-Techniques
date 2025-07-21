'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.equal\ntorch.equal(input, other)\n'
import torch
x = torch.empty(5, 3)
y = torch.empty(5, 3)
print(torch.equal(x, y))
x = torch.zeros(5, 3, dtype=torch.long)
y = torch.zeros(5, 3, dtype=torch.long)
print(torch.equal(x, y))
x = x.new_ones(5, 3, dtype=torch.double)
y = torch.randn_like(x, dtype=torch.double)
print(torch.equal(x, y))