'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sparse.mm\ntorch.sparse.mm(mat1, mat2)\n'
import torch
mat1 = torch.sparse.FloatTensor(3, 3).to_dense()
mat2 = torch.sparse.FloatTensor(3, 3).to_dense()
torch.sparse.mm(mat1, mat2)