A = torch.tensor([[1.0, 2.0], [3.0, 4.0]], requires_grad=True)
B = torch.tensor([[1.0, 2.0], [3.0, 4.0]], requires_grad=True)
X = torch.linalg.solve(A, B)