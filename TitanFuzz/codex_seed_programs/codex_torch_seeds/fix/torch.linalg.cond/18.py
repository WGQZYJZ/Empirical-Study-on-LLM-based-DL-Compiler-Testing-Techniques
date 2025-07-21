'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.cond\ntorch.linalg.cond(A, p=None, *, out=None)\n'
import torch
import torch
A = torch.randn(4, 4)
A = torch.matmul(A.t(), A)
cond_A = torch.linalg.cond(A)
print('Condition number of A:', cond_A)
cond_A_p2 = torch.linalg.cond(A, p=2)
print('Condition number of A with p=2:', cond_A_p2)
cond_A_pfro = torch.linalg.cond(A, p='fro')
print("Condition number of A with p='fro':", cond_A_pfro)