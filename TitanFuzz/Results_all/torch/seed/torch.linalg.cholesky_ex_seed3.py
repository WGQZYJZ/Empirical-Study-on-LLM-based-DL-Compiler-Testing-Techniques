A = torch.randn(3, 3)
A = torch.matmul(A, A.t())
L = torch.linalg.cholesky_ex(A)