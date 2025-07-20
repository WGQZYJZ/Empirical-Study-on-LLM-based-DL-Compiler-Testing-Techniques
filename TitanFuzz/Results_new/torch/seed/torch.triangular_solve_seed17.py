A = torch.tensor([[3, 0, 0], [1, 2, 0], [0, 1, 1]], dtype=torch.float)
b = torch.tensor([[2, 3, 3]], dtype=torch.float).t()
x = torch.triangular_solve(b, A, upper=True)[0]