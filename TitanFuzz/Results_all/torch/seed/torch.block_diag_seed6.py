A = torch.randn(2, 3)
B = torch.randn(4, 5)
C = torch.randn(6, 7)
block_diag_matrix = torch.block_diag(A, B, C)