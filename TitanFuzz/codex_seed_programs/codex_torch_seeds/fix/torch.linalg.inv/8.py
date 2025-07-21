'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.inv\ntorch.linalg.inv(A, *, out=None)\n'
import torch
A = torch.rand(3, 3)
torch.linalg.inv(A)
out = torch.empty(3, 3)
torch.linalg.inv(A, out=out)
torch.linalg.pinv(A)
out = torch.empty(3, 3)
torch.linalg.pinv(A, out=out)
torch.linalg.svd(A)
out = torch.empty(3, 3)