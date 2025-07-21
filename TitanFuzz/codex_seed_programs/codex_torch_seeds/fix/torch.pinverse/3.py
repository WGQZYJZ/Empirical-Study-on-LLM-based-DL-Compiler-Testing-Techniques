'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pinverse\ntorch.pinverse(input, rcond=1e-15)\n'
import torch
a = torch.rand(3, 3)
b = torch.pinverse(a)
print(b)