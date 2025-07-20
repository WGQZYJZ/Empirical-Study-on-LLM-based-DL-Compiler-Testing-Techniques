A = torch.Tensor([[4.0, (- 1.0), 1.0], [(- 1.0), 4.0, (- 1.0)], [1.0, (- 1.0), 4.0]])
L = torch.linalg.cholesky(A)