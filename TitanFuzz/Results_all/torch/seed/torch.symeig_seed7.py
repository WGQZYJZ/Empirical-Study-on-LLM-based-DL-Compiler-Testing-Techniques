A = torch.tensor([[1.0, (- 1.0), 0.0], [(- 1.0), 1.0, 0.0], [0.0, 0.0, 2.0]])
(eigenvalues, eigenvectors) = torch.symeig(A, eigenvectors=True)