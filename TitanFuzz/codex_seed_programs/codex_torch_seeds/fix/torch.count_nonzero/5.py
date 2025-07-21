'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.count_nonzero\ntorch.count_nonzero(input, dim=None)\n'
import torch
x = torch.tensor([[0, 1, 7, 0, 0], [3, 0, 0, 2, 19]])
print(torch.count_nonzero(x))
print(torch.count_nonzero(x, dim=0))
print(torch.count_nonzero(x, dim=1))