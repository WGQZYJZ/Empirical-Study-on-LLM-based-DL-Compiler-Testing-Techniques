'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.equal\ntorch.equal(input, other)\n'
import torch
x1 = torch.tensor([1, 1, 1])
x2 = torch.tensor([1, 1, 1])
print((x1 == x2))
print(torch.equal(x1, x2))