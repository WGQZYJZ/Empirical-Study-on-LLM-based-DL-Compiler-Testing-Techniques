'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.multi_dot\ntorch.linalg.multi_dot(tensors, *, out=None)\n'
import torch
A = torch.rand(10, 20)
B = torch.rand(20, 30)
C = torch.rand(30, 40)
D = torch.rand(40, 50)
E = torch.linalg.multi_dot([A, B, C, D])
print(E.shape)
E_ = torch.matmul(A, torch.matmul(B, torch.matmul(C, D)))
print(torch.allclose(E, E_))