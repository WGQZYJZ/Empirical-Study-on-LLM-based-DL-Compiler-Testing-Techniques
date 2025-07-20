A = torch.randn(5, 5, dtype=torch.float64)
A_symm = ((A + A.T) / 2)
eigvalsh = torch.linalg.eigvalsh(A_symm)