A = torch.tensor([[4.0, (- 2.0), 1.0], [(- 2.0), 4.0, (- 2.0)], [1.0, (- 2.0), 4.0]])
b = torch.tensor([[1.0], [4.0], [2.0]])
x = torch.cholesky_solve(b, A)