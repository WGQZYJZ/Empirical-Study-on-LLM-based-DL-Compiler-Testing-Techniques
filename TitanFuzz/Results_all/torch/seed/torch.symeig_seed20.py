A = torch.rand(3, 3)
(eigenvalues, eigenvectors) = torch.symeig(A, eigenvectors=True)