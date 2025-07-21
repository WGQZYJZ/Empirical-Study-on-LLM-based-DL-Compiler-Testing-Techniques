"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigvalsh\ntorch.linalg.eigvalsh(A, UPLO='L', *, out=None)\n"
import torch
A = torch.randn(3, 3)
A_sym = ((A + A.t()) / 2)
eigen_values = torch.linalg.eigvalsh(A_sym)
print(f'eigen_values = {eigen_values}')