'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sparse.addmm\ntorch.sparse.addmm(mat, mat1, mat2, beta=1.0, alpha=1.0)\n'
import torch
import torch
A = torch.sparse.FloatTensor(3, 3).to_dense()
B = torch.sparse.FloatTensor(3, 3).to_dense()
C = torch.sparse.FloatTensor(3, 3).to_dense()
torch.sparse.addmm(A, B, C)