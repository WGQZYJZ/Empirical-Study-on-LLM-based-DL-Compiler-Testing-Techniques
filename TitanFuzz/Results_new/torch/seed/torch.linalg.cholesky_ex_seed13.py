A = torch.tensor([[4.0, 12.0, (- 16.0)], [12.0, 37.0, (- 43.0)], [(- 16.0), (- 43.0), 98.0]])
L = torch.linalg.cholesky_ex(A, upper=False)
L = torch.linalg.cholesky_ex(A, upper=True)