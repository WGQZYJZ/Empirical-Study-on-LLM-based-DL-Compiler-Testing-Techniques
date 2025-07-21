'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.lstsq\ntorch.linalg.lstsq(A, B, rcond=None, *, driver=None)\n'
import torch
import math
x = torch.tensor([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])
y = torch.tensor([1.0, 3.0, 2.0, 5.0, 7.0, 8.0, 8.0, 9.0, 10.0, 12.0])
A = torch.stack([x, torch.ones_like(x)], dim=1)
print(A)
b = y.unsqueeze(1)
print(b)
(x, residuals, rank, s) = torch.linalg.lstsq(A, b)
print('x:', x)
print('residuals:', residuals)
print('rank:', rank)
print('s:', s)