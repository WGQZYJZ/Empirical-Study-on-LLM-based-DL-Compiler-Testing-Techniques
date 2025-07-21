'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.qr\ntorch.qr(input, some=True, *, out=None)\n'
import torch
A = torch.randn(3, 5)
(A_q, A_r) = torch.qr(A)
print(A_q.size(), A_r.size())
A = torch.randn(3, 3)
b = torch.randn(3, 2)
x = torch.triangular_solve(b, A)[0]
print(x.size())