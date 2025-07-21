'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.cholesky\ntorch.linalg.cholesky(A, *, upper=False, out=None)\n'
import torch
import numpy as np
A = np.array([[4, 12, (- 16)], [12, 37, (- 43)], [(- 16), (- 43), 98]])
A = torch.from_numpy(A)
A = A.float()
L = torch.linalg.cholesky(A)
print(L)