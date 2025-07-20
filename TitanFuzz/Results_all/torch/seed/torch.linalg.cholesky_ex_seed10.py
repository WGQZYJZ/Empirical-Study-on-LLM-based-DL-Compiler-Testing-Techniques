A = torch.tensor([[1, 2, 3], [2, 3, 4], [3, 4, 5]], dtype=torch.float32)
L = torch.linalg.cholesky_ex(A)