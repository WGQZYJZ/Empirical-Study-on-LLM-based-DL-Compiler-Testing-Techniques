input = torch.randn(3, 3)
(eigenvalues, eigenvectors) = torch.eig(input, True)
eigenvalues = torch.eig(input, False)