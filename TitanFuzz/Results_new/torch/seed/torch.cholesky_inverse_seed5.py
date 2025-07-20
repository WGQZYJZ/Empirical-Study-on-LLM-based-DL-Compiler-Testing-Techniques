A = torch.randn(3, 3)
A = torch.mm(A.t(), A)
B = torch.cholesky_inverse(A)