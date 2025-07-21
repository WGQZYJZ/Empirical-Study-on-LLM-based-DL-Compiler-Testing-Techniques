'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.block_diag\ntorch.block_diag(*tensors)\n'
import torch
A = torch.randn(2, 3)
B = torch.randn(4, 5)
C = torch.randn(6, 7)
block_diag_matrix = torch.block_diag(A, B, C)
print(block_diag_matrix)