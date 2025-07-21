'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.svd_lowrank\ntorch.svd_lowrank(A, q=6, niter=2, M=None)\n'
import torch
import numpy as np
import time
A = torch.randn(1000, 1000)
t1 = time.time()
(U, S, V) = torch.svd(A)
t2 = time.time()
print('Time for torch.svd: ', (t2 - t1))
t1 = time.time()
(U, S, V) = torch.svd_lowrank(A, q=6, niter=2, M=None)
t2 = time.time()
print('Time for torch.svd_lowrank: ', (t2 - t1))