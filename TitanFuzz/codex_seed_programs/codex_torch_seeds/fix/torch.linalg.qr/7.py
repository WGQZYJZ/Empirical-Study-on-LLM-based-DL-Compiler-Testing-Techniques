"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.qr\ntorch.linalg.qr(A, mode='reduced', *, out=None)\n"
import torch
A = torch.tensor([[12.0, (- 51.0), 4.0], [6.0, 167.0, (- 68.0)], [(- 4.0), 24.0, (- 41.0)]])
(q, r) = torch.linalg.qr(A)
print(q)
print(r)