A = torch.tensor([[1, 2, 3], [3, 2, 1], [1, 1, 1]], dtype=torch.float64)
B = torch.tensor([[1, 2, 3], [3, 2, 1], [1, 1, 1]], dtype=torch.float64)
torch.linalg.solve(A, B, out=None)