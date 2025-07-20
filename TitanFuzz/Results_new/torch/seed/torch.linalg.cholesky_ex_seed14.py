A = torch.tensor([[2, 1, 1], [1, 2, 1], [1, 1, 2]], dtype=torch.float)
L = torch.linalg.cholesky_ex(A, upper=False)
L = torch.linalg.cholesky_ex(A, upper=True)