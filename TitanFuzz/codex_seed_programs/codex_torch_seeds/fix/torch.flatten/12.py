'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flatten\ntorch.flatten(input, start_dim=0, end_dim=-1)\n'
import torch
x = torch.randn(2, 3, 4, 5)
print(x.shape)
print(torch.flatten(x, start_dim=1, end_dim=(- 2)).shape)
print(torch.flatten(x, start_dim=2, end_dim=(- 1)).shape)
'\ndim (int or tuple of ints) – the dimension or dimensions to squeeze.\nIf dim is a tuple of ints, a squeeze operation is performed for each of the specified dimensions.\n'
x = torch.randn(2, 1, 2, 1, 2)
print(x.shape)
print(torch.squeeze(x).shape)
print(torch.squeeze(x, dim=0).shape)
print(torch.squeeze(x, dim=1).shape)
print(torch.squeeze(x, dim=2).shape)