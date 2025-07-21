"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigh\ntorch.linalg.eigh(A, UPLO='L', *, out=None)\n"
import torch
torch.__version__
A = torch.rand(3, 3)
A
torch.linalg.eigh(A)
torch.linalg.eigh(A, UPLO='U')
torch.linalg.eigh(A, UPLO='L')
torch.linalg.eigh(A, UPLO='L', out=(torch.rand(3), torch.rand(3, 3)))
torch.linalg.eigh(A, UPLO='L', out=(torch.rand(3), torch.rand(3, 3)))[0]
torch.linalg.eigh(A, UPLO='L', out=(torch.rand(3), torch.rand(3, 3)))[1]