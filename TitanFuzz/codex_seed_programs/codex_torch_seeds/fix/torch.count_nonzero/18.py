'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.count_nonzero\ntorch.count_nonzero(input, dim=None)\n'
import torch
input = torch.tensor([[0, 1, 7, 0, 0], [3, 0, 0, 2, 19]])
print(torch.count_nonzero(input))
print(torch.count_nonzero(input, dim=0))
print(torch.count_nonzero(input, dim=1))
'\nTask 4: Call the API torch.nonzero\ntorch.nonzero(input, as_tuple=False)\n'
print(torch.nonzero(input))
print(torch.nonzero(input, as_tuple=True))
'\nTask 5: Call the API torch.eye\ntorch.eye(n, m=None, out=None)\n'
print(torch.eye(2))
print(torch.eye(2, 3))
'\nTask 6: Call the API torch.diag\ntorch.diag(input, diagonal=0, out=None)\n'
print(torch.diag(torch.arange(1, 6)))