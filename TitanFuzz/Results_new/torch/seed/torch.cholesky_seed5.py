A = torch.rand(3, 3)
A = A.mm(A.t())
L = torch.cholesky(A)