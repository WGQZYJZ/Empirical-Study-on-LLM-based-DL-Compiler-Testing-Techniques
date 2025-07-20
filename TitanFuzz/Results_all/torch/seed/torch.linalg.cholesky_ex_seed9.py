A = torch.randn((5, 5))
A = torch.mm(A, A.t())
L = torch.linalg.cholesky_ex(A, upper=False)