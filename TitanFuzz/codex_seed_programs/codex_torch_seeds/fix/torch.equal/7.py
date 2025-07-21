'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.equal\ntorch.equal(input, other)\n'
import torch
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[1, 2], [3, 4]])
print(torch.equal(a, b))
c = torch.tensor([[1, 2], [3, 4]])
d = torch.tensor([[1, 2], [3, 5]])
print(torch.equal(c, d))