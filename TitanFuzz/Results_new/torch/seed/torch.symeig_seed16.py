input = torch.rand(3, 3)
(eigenvalues, eigenvectors) = torch.symeig(input, eigenvectors=True, upper=True)