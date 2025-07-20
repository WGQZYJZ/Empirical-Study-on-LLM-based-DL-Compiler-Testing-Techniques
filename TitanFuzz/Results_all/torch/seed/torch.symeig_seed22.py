input = torch.randn(3, 3)
(eigenvalues, eigenvectors) = torch.symeig(input, eigenvectors=True)
(eigenvalues, eigenvectors) = torch.symeig(input, eigenvectors=False)
(eigenvalues, eigenvectors) = torch.symeig(input, eigenvectors=True, upper=False)