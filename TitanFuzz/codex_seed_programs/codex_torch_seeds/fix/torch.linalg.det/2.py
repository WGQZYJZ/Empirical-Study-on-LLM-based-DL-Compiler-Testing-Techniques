'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.det\ntorch.linalg.det(A, *, out=None)\n'
import torch
A = torch.rand(3, 3)
det_A = torch.linalg.det(A)
print(det_A)