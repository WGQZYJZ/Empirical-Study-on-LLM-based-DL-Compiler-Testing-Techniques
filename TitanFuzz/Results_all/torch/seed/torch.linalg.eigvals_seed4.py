A = torch.randn((3, 3))
eigenvalues = torch.linalg.eigvals(A)
A = torch.randn((3, 3))
eigenvalues = torch.linalg.eigvalsh(A)