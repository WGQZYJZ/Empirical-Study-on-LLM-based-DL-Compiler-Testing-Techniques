'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cartesian_prod\ntorch.cartesian_prod(*tensors)\n'
import torch
a = torch.tensor([1, 2, 3, 4])
b = torch.tensor([5, 6, 7, 8])
c = torch.cartesian_prod(a, b)
print(c)