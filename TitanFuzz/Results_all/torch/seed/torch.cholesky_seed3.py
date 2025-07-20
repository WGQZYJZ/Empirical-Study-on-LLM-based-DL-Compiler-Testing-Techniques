A = torch.tensor([[4.0, 12.0, (- 16.0)], [12.0, 37.0, (- 43.0)], [(- 16.0), (- 43.0), 98.0]])
L = torch.cholesky(A)
A = torch.tensor([[4.0, 12.0, (- 16.0)], [12.0, 37.0, (- 43.0)], [(- 16.0), (- 43.0), 98.0]])
L_inverse = torch.cholesky_inverse(A)
A = torch.t