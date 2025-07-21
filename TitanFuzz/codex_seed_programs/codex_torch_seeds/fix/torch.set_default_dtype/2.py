'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_default_dtype\ntorch.set_default_dtype(d)\n'
import torch
x = torch.tensor([1, 2, 3, 4, 5])
torch.set_default_dtype(torch.float64)
x = torch.tensor([1, 2, 3, 4, 5])
print('x = ', x)
print('x dtype = ', x.dtype)