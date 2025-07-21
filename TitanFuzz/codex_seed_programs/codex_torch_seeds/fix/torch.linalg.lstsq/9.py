'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.lstsq\ntorch.linalg.lstsq(A, B, rcond=None, *, driver=None)\n'
import torch
A = torch.rand(2, 3, dtype=torch.float, requires_grad=True)
B = torch.rand(2, 3, dtype=torch.float, requires_grad=True)
torch.linalg.lstsq(A, B)