A = torch.rand(2, 2, requires_grad=True)
B = torch.rand(2, 2, requires_grad=True)
C = torch.linalg.solve(A, B)
D = torch.linalg.solve(A, B, out=None)