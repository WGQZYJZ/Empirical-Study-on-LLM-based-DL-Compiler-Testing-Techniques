"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.qr\ntorch.linalg.qr(A, mode='reduced', *, out=None)\n"
import torch
A = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
(Q, R) = torch.linalg.qr(A)
print(Q)
print(R)