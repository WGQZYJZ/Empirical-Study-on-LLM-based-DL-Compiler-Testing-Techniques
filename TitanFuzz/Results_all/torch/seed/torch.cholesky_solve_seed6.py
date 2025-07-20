A = torch.randn(3, 3)
A = torch.matmul(A.t(), A)
b = torch.randn(3, 1)
x = torch.cholesky_solve(b, A)