'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_num_interop_threads\ntorch.set_num_interop_threads(int)\n'
import torch
import time
import numpy as np
torch.set_num_interop_threads(4)
print('PyTorch version:', torch.__version__)
N = 100000
A = torch.ones(N, N)
B = torch.ones(N, N)
C = torch.matmul(A, B)
start = time.time()
C = torch.matmul(A, B)
print('Elapsed time:', (time.time() - start))
print(C[0][0])