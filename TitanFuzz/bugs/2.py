import torch
A  = torch.tensor([[0.0, 1.0, -1.0], [1.0, -1.0, 0.0], [-1.0, 1.0, 0.0]])
Apinv = torch.pinverse(A)
print(A @ Apinv @ A)
print(torch.dist(A @ Apinv @ A, A))