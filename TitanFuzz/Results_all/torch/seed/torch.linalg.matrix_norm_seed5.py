A = torch.randn(2, 3, 5)
torch.linalg.matrix_norm(A, ord='fro', dim=((- 2), (- 1)), keepdim=False)
A = torch.randn(2, 3, 5)
n = 3