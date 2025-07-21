'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.svd\ntorch.svd(input, some=True, compute_uv=True, *, out=None)\n'
import torch
if True:
    A = torch.randn(3, 4)
    print('Input matrix A: \n', A)
    (U, S, V) = torch.svd(A)
    print('U: \n', U)
    print('S: \n', S)
    print('V: \n', V)
    print('U * S * V.T: \n', U.mm(torch.diag(S)).mm(V.t()))