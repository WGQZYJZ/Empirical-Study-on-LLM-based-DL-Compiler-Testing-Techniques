'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.pinv\ntorch.linalg.pinv(A, rcond=1e-15, hermitian=False, *, out=None)\n'
import torch
if True:
    import torch
    A = torch.rand(3, 3)
    print('A: \n{}'.format(A))
    A_pinv = torch.linalg.pinv(A)
    print('A_pinv: \n{}'.format(A_pinv))