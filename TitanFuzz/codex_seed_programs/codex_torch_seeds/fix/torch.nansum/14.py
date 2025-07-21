'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nansum\ntorch.nansum(input, dim, keepdim=False, *, dtype=None)\n'
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(x)
sum_x = torch.nansum(x, dim=1)
print(sum_x)
sum_x = torch.nansum(x, dim=1, keepdim=True)
print(sum_x)