A = torch.randn(3, 3, dtype=torch.float64)
(eigenvalues, eigenvectors) = torch.eig(A, True)