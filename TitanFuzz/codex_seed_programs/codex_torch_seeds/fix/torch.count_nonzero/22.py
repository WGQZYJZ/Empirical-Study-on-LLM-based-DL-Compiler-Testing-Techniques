'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.count_nonzero\ntorch.count_nonzero(input, dim=None)\n'
import torch
import torch
data = torch.randint(0, 2, (2, 3))
print(data)
print(torch.count_nonzero(data))
print(torch.count_nonzero(data, dim=0))
print(torch.count_nonzero(data, dim=1))