'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.slogdet\ntorch.linalg.slogdet(A, *, out=None)\n'
import torch
A = torch.randn(3, 3)
print(A)
'\nTask 4: Calculate the determinant of A\n'
det = torch.linalg.det(A)
print(det)
'\nTask 5: Calculate the log of determinant of A\n'
log_det = torch.linalg.slogdet(A)
print(log_det)