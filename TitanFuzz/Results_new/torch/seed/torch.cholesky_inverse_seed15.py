A = torch.randn(3, 3)
A = torch.matmul(A, A.t())
A_inv = torch.cholesky_inverse(A)