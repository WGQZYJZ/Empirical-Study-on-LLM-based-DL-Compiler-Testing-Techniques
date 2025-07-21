"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigvalsh\ntorch.linalg.eigvalsh(A, UPLO='L', *, out=None)\n"
import torch
import numpy as np
A = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
print('A: ', A)
eigvalsh = torch.linalg.eigvalsh(A)
print('eigvalsh: ', eigvalsh)
eigvalsh = torch.linalg.eigvalsh(A, UPLO='U')
print('eigvalsh: ', eigvalsh)
eigvalsh = torch.linalg.eigvalsh(A, UPLO='L')
print('eigvalsh: ', eigvalsh)