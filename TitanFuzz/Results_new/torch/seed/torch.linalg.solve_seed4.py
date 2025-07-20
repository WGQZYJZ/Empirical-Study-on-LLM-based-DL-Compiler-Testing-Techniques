A = torch.randn(3, 3, dtype=torch.float)
B = torch.randn(3, 2, dtype=torch.float)
X = torch.linalg.solve(A, B)