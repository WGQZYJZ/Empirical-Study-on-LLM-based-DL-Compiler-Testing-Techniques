A = torch.rand(4, 4)
A = (A.t() @ A)
L = torch.linalg.cholesky(A)