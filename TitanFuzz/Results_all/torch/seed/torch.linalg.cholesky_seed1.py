A = torch.randn(2, 2)
A_t = A.t()
A_symm = torch.matmul(A, A_t)
L = torch.linalg.cholesky(A_symm, upper=False)