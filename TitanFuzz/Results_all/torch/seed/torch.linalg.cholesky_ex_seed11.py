A = torch.randn(3, 3)
A = (A.T @ A)
L = torch.linalg.cholesky_ex(A)