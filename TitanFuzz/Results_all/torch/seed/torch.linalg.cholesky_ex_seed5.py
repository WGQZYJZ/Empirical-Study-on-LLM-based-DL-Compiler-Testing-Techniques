A = torch.rand(3, 3, dtype=torch.float64)
A = A.mm(A.t())
L = torch.linalg.cholesky_ex(A)