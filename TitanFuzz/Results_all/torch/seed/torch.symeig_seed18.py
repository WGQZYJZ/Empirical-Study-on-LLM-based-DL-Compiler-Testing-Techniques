A = torch.tensor([[1, 2, 3], [2, 4, 5], [3, 5, 6]], dtype=torch.float32)
(eigenvalues, eigenvectors) = torch.symeig(A, eigenvectors=True)
eigenvalues = torch.symeig(A, eigenvectors=False)