A = torch.tensor([[4, 12, (- 16)], [12, 37, (- 43)], [(- 16), (- 43), 98]], dtype=torch.float32)
L = torch.linalg.cholesky(A)