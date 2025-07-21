'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.lstsq\ntorch.linalg.lstsq(A, B, rcond=None, *, driver=None)\n'
import torch
A = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
B = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
(x, res, rank, s) = torch.linalg.lstsq(A, B)
print(x)
print(res)
print(rank)
print(s)