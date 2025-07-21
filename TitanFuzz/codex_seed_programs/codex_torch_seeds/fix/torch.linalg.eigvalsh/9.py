"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigvalsh\ntorch.linalg.eigvalsh(A, UPLO='L', *, out=None)\n"
import torch
A = torch.randn(3, 3)
print(torch.linalg.eigvalsh(A))
print(torch.linalg.eigvalsh(A, UPLO='U'))