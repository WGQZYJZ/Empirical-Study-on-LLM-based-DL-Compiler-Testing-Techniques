input = torch.randn(5, 5)
(eigenvalues, eigenvectors) = torch.symeig(input, eigenvectors=True)