'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sparse.addmm\ntorch.sparse.addmm(mat, mat1, mat2, beta=1.0, alpha=1.0)\n'
import torch
import numpy as np
import time
import torch
mat = torch.sparse.FloatTensor(3, 3).to_dense()
mat1 = torch.randn(3, 5)
mat2 = torch.randn(5, 3)
torch.sparse.addmm(mat, mat1, mat2, beta=1.0, alpha=1.0)