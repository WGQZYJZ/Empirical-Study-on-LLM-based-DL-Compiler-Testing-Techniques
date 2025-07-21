'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.pinv\ntorch.linalg.pinv(A, rcond=1e-15, hermitian=False, *, out=None)\n'
import torch
A = torch.randn(3, 3)
pinv_A = torch.linalg.pinv(A)
print('pinv_A: \n', pinv_A)
(U, S, V) = torch.svd(A)
mask = (S > 1e-15).type(torch.bool)
S_inv = torch.zeros(A.shape[0], A.shape[1])
S_inv[mask] = (1.0 / S[mask])
pinv_A_2 = torch.mm(V.t(), torch.mm(S_inv.t(), U.t()))
print('pinv_A_2: \n', pinv_A_2)