A = torch.tensor([[2, 3, 2], [1, 1, 1], [3, 2, 2]], dtype=torch.float)
b = torch.tensor([[1, 2, 3]], dtype=torch.float).t()
x = torch.triangular_solve(b, A, upper=True)[0]