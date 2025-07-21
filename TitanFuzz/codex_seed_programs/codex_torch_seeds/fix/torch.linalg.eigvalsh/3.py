"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigvalsh\ntorch.linalg.eigvalsh(A, UPLO='L', *, out=None)\n"
import torch
A = torch.randn(5, 5, dtype=torch.float64)
A_symm = ((A + A.T) / 2)
eigvalsh = torch.linalg.eigvalsh(A_symm)
print(eigvalsh)