A = torch.Tensor([[1, 2], [2, 1]])
L = torch.linalg.cholesky_ex(A, upper=False)
U = torch.linalg.cholesky_ex(A, upper=True)