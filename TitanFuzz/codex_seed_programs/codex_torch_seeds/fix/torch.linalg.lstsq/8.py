'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.lstsq\ntorch.linalg.lstsq(A, B, rcond=None, *, driver=None)\n'
import torch
import torch
A = torch.randn(3, 3)
B = torch.randn(3, 1)
X = torch.linalg.lstsq(A, B)
print(X)